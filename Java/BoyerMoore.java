/* Bad Character Heuristic of Boyer Moore String Matching Algorithm in Java */

/*
References:
1. Boyer Moore Substring Search - https://algs4.cs.princeton.edu/53substring/BoyerMoore.java.html
2. Boyer Moore Algorithm for Pattern Searching - https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
*/

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

class Index {
    int from;
    int to;
    public Index(int from, int to)
    {
        this.from = from;
        this.to = to;
    }
}

class BoyerMoore{
	public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        final int CHARS_SIZE = 256;
        int lastOccurence[] = new int[CHARS_SIZE];
        LinkedList<Index> indexes = new LinkedList<>();

        //Input
		System.out.println("Enter text");
        char text[] = sc.nextLine().toCharArray();

        System.out.println("Enter search pattern");
        char pattern[] = sc.nextLine().toCharArray();

        //Preprocess
        preprocess(pattern, lastOccurence);

        int textIndex = 0;
        int textLength = text.length, patternLength = pattern.length;
        int patternIndex = 0;
        int move = 0;
        boolean found = false;

        //Search
        for(textIndex = 0; textIndex <= (textLength - patternLength); textIndex += move)
        {
            move = -1;
            for(patternIndex = (patternLength - 1); patternIndex >= 0; patternIndex--)
            {
                if(pattern[patternIndex] != text[textIndex + patternIndex])
                {
                    move = Math.max(1, patternIndex - lastOccurence[text[textIndex + patternIndex]]);
                    break;
                }
            }
            //Pattern Found
            if(move == -1)
            {
                found = true;
                move = patternLength;
                indexes.add(new Index(textIndex, textIndex + patternLength - 1));
                // break;
            }
        }
        if(!found)
        {
            System.out.println("Not Found");
        }
        else
        {
            for(Index index : indexes)
            {
                System.out.println("Pattern found, from index: " + index.from + 
                " to index: " + index.to);
            }
        }
	}

    public static void preprocess(char pattern[], int lastOccurence[])
    {
        Arrays.fill(lastOccurence, -1);
        for(int i = 0; i < pattern.length; i++)
        {
            lastOccurence[pattern[i]] = i;
        }
    }
}
