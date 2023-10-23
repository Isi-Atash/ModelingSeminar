using System;

public class Program
{
    public static int ModuloInverse(int num, int modulo)
    {
        var (gcd, x, _) = ModifiedGcd(num, modulo);
        if (gcd == 1)
        {
            return x % modulo;
        }
        else
        {
            return -1;
        }
    }
    
    public static (int, int, int) ModifiedGcd(int x, int y)
    {
        if (x == 0)
        {
            return (y, 0, 1);
        }
        else
        {
            var (result, a, b) = ModifiedGcd(y % x, x);
            return (result, b - (y / x) * a, a);
        }
    }
    
    public static int[][] InitializeInverseHeader(int headerSize)
    {
        var inverseHeader = new int[headerSize][];
        for (int i = 0; i < headerSize; i++)
        {
            inverseHeader[i] = new int[headerSize];
            for (int j = 0; j < headerSize; j++)
            {
                inverseHeader[i][j] = 0;
            }
            inverseHeader[i][i] = 1;
        }
        return inverseHeader;
    }
    
    public static void GaussianElimination(int[][] encodedData, int[][] inverseHeader, int modulus, int headerSize)
    {
        for (int col = 0; col < headerSize; col++)
        {
            int colValue = ModuloInverse(encodedData[col][col], modulus);
            for (int j = 0; j < headerSize; j++)
            {
                encodedData[col][j] = (encodedData[col][j] * colValue) % modulus;
                inverseHeader[col][j] = (inverseHeader[col][j] * colValue) % modulus;
            }
            for (int row = 0; row < headerSize; row++)
            {
                if (row != col)
                {
                    int factor = encodedData[row][col];
                    for (int i = 0; i < headerSize; i++)
                    {
                        encodedData[row][i] = (encodedData[row][i] - factor * encodedData[col][i]) % modulus;
                        inverseHeader[row][i] = (inverseHeader[row][i] - factor * inverseHeader[col][i]) % modulus;
                    }
                }
            }
        }
    }
    
    public static void Main()
    {
        // Test your code here
        int headerSize = int.Parse(Console.ReadLine());
        int messageSize = int.Parse(Console.ReadLine);
        int[][] encodedData = new int[headerSize][];
        for (int i = 0; i < headerSize; i++)
        {
            string inputLine = Console.ReadLine().Trim();
            encodedData[i] = new int[inputLine.Length];
            for (int j = 0; j < inputLine.Length; j++)
            {
                encodedData[i][j] = (int)inputLine[j];
            }
        }
        int modulus = 127;

        string decryptedMessage = MessageDecoder.DecryptMessage(headerSize, messageSize, encodedData, modulus);

        Console.WriteLine(decryptedMessage);
    }
}