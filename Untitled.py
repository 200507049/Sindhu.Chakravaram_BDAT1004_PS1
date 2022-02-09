#!/usr/bin/env python
# coding: utf-8

# ### Question1

# In[ ]:


5 - Int
5.0 - Float
5 > 1 - Boolean
'5'- Char
5 * 2    -Int 
'5' * 2   - Invalid
'5' + '2'   -Char
5 / 2  -Float
5 % 2   -Int
{5, 2, 1}   -array
5 == 3    -boolean
Pi (the number)  - double


# ### Question2

# #### Question2a

# In[ ]:


using System;

    public class Program
    {
        public static void Main()
        {
            Console.WriteLine("There number of letters in the string Supercalifragilisticexpialidocious are " + "Supercalifragilisticexpialidocious".Length);
        }
    }


# ![2A.PNG](attachment:2A.PNG)

# #### Question2b

# In[5]:


using System;

    public class Program
    {
        public static void Main()
        {
            string s= "Supercalifragilisticexpialidocious";
            if(s.Contains("ice")== true){
                Console.WriteLine("Ice is a substring");}
            else{
                Console.WriteLine("Ice is not a substring");
            }  
        }
    }


# ![2B.PNG](attachment:2B.PNG)

# 

# #### Question2c

# In[ ]:


using System;
   class program2 {
      public static void Main() {
         int s1 = "Supercalifragilisticexpialidocious".Length;
        int s2 = "Honorificabilitudinitatibus".Length;
         int s3 = "Bababadalgharaghtakamminarronnkonn".Length;
         if (s1 > s2) {
            if (s1 > s3) {
               Console.Write("Supercalifragilisticexpialidocious");
            } else if (s1 == s3) {
               Console.Write("both Supercalifragilisticexpialidocious and Bababadalgharaghtakamminarronnkonn have same count");
         }             else{
                 Console.WriteLine("Bababadalgharaghtakamminarronnkonn");}
      }      else if (s2 > s3)
         Console.Write("Honorificabilitudinitatibus");
          else if (s2 == s3) {
               Console.Write("both Honorificabilitudinitatibus and Bababadalgharaghtakamminarronnkonn have same count");}
          else
         Console.Write("Bababadalgharaghtakamminarronnkonn");
      }
   }


# ![2C.PNG](attachment:2C.PNG)

# #### Question2d

# In[ ]:


using System;
class Program    
{
    public static void Main()
        {
        string[] alpha = new string[]
        {"Berlioz","Borodin","Brian","Bartok","Bellini","Buxtehude","Bernstein"};
        Array.Sort(alpha);
        foreach (string order in alpha)
        {
            Console.WriteLine(order);
             
        }
        Console.WriteLine("Last element: "+alpha[alpha.Length - 1]);
        Console.WriteLine("First element: "+alpha[0]);
    }
}


# ![2D.PNG](attachment:2D.PNG)

# ### Question3

# In[ ]:


using System;
    public class Program3
    {
        public static void Main(string[] args)
        {   double s, area;
            double a, b, c;
            Console.WriteLine("Enter side1");
            a = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter side2");
            b = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter side3");
            c = double.Parse(Console.ReadLine());
            s = (a + b + c) / 2;
            area = Math.Sqrt(s * ( s - a) * (s - b) * (s - c)); 
            Console.WriteLine("Area of the Triangle = " + area); 
    }
 }


# ![3.PNG](attachment:3.PNG)

# ### Question4

# In[ ]:


using System;
class Rectangle
    {
        static bool inside(int x1, int y1, int x2, int y2, int x, int y)
        {
            if (x > x1 && x < x2 && y > y1 && y < y2)
            return true; 
            return false;
        }
public static void Main()
        {
          int x,y,x1,y1,x2,y2;
              Console.WriteLine("x");
          x = int.Parse(Console.ReadLine());
             Console.WriteLine("y");
                        y = int.Parse(Console.ReadLine());
             Console.WriteLine("x1");
                        x1 = int.Parse(Console.ReadLine());
             Console.WriteLine("y1");
                        y1 = int.Parse(Console.ReadLine());
             Console.WriteLine("x2");
                        x2 = int.Parse(Console.ReadLine());
             Console.WriteLine("y2");
                        y2 = int.Parse(Console.ReadLine());
    if (inside(x1, y1, x2, y2, x, y))
        Console.Write("True");
    else
        Console.Write("False");
}
}


# ![4.PNG](attachment:4.PNG)

# ### Question5

# #### Question5a

# In[ ]:


using System;
public class Program
{
    public static void Main(string[] args)
        {
            int[] arr1 = new int[5];
            arr1[0] = 25;
            arr1[1] = 47;
            arr1[2] = 42;
            arr1[3] = 56;
            arr1[4] = 32;

            int[] arr2 = new int[5];
            int[] arr3 = new int[5];
            int i, j = 0, k = 0;
            for (i = 0; i < 5; i++)
            {
            if (arr1[i] % 2 == 0)
            {
            arr2[j] = arr1[i];
            j++;
            }
            else
            {
            arr3[k] = arr1[i];
            k++;
            }
            }
            Console.WriteLine("The Even numbers are");
            for (i = 0; i < j; i++)
            {
            Console.WriteLine(arr2[i]);
            }
            Console.WriteLine("The Odd numbers are");
            for (i = 0; i < k; i++)
            {
            Console.WriteLine(arr3[i]);
            }
}
}


# ![5A.PNG](attachment:5A.PNG)

# #### Question5b

# In[ ]:


using System;
class Rectangle{
static bool inside(int x , int y, double x1, double y1, double x2, double y2){
if (x > x1 && x < x2 && y > y1 && y < y2)
return true; return false;}
public static void Main()
{
      double x1 = 0.5, y1 = 0.2, x2 = 1.1, y2 = 2;

    int x = 1, y = 1;

    if (inside(x, y, x1, y1, x2, y2))
        Console.Write("Yes");
    else
        Console.Write("No");
}
}


# ![5B.PNG](attachment:5B.PNG)

# ### Question6

# In[6]:


word = input("Enter word to be translated:\n")

vowels = ['a','e','i','o','u','A','E','I','O','U']
def pig(word): 
    first = word[0]

    if first in vowels: 
        word = word.lower()
        word += "way" 
        return word
    else: 
        word = word.lower()

        for letter in word:
            if letter in vowels:
                index_value = word.index(letter)
                break

        word = word[index_value:] +word[:index_value]+ "ay" 
        return word 

print(pig(word))


# ### Question7

# In[83]:


def bldcount(file):
    file=open('D:/BDAT/1004-Ethan Davis-Data Programming/bloodtype1.txt','r')
    for i in file:
        bldtp=i.split()

        if 'A' in bldtp:
            count=bldtp.count('A')
            print("There are {} patients of bloodtype A".format(count))
        else:
            print("There are {} patients of bloodtype A".format(count))
        if 'B' in bldtp:
            count=bldtp.count('B')
            print("There are {} patients of bloodtype B".format(count))
        else:
            print("There are no patients of bloodtype AB")    
        if 'AB' in bldtp:
            count=bldtp.count('AB')
            print("There are {} patients of bloodtype AB".format(count))
        else:
            print("There are no patients of bloodtype AB")    
        if 'O' in bldtp:
            count=bldtp.count('O')
            print("There are {} patients of bloodtype O".format(count))
        else:
            print("There are no patients of bloodtype O")    
        if 'OO' in bldtp:
            count=bldtp.count('OO')
            print("There are {} patients of bloodtype OO".format(count))
        else:
            print("There are no patients of bloodtype OO")

    file.close()

bldcount(file)


# ### Question8

# In[ ]:





# ### Question9

# In[ ]:


#Trying to add incompatible variables, as in adding 6 + ‘a’
--------------------------------------------------------------------------
6+'a'
CAUSES TypError------> unsupported operand types




#Referring to the 12th item of a list that has only 10 items
--------------------------------------------------------------------------
lst=[1,2,3,'abc']
lst[4]
CAUSES IndexError -----> list assignment index out of range




#Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)
--------------------------------------------------------------------------
ValueError: math domain error




#Using an undeclared variable, such as print(x) when x has not been defined
--------------------------------------------------------------------------
NameError: name 'x' is not defined




#Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.
--------------------------------------------------------------------------
FileNotFoundError: [Errno 2] No such file or directory:


# ### Question10

# In[90]:


def frequencies(str):
    a='abcdefghijklmnopqrstuvwxyz'
    A=[]

    for i in a:
        if i in str:
            A.append(str.count(i))

        if i not in str:
            A.append(str.count(i))
    print(A)



frequencies('The quick red fox got bored and went home.')
frequencies('apple')


# In[ ]:




