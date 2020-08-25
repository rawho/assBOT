import fire
import os
import shutil


def create(name):
    try:
        os.mkdir(f"{name}")
        shutil.copy2('cet-logo.jpeg', f'{name}/cet-logo.jpeg')
        shutil.copy2('demo.png', f'{name}/demo.png')
        os.chdir(f"{name}")
        f = open(f"{name}.md", "w")

        f.write(
        r"""
<style>
    body{  
    }  
    .main-page{
        max-width: 80%;
        min-height: 100vh;
        margin: auto;
        text-align: center;
    } 
    .clg-name{
        font-size: 30px;
        font-weight: 300;
    }
    .ass-heading{
        font-size: 45px;
        font-weight: 900;
        margin-top: 50px;
    }
    .name{
        font-size: 28px;
    }
    .dept-name{
        font-size: 28px;
        font-weight: 300;
        margin-top: 100px;
    }
</style>

<div class="main-page">
    <p class="clg-name">
        College Of Engineering Trivandrum
    </p>
    <h1 class="ass-heading">
        Object Oriented Programming using Python
    </h1>
    <img src="./cet-logo.jpeg" alt="">
    <br><br><br>
    <p class="name">Rahul T</p>
    <p class="name">S3 CSE Roll No:53</p>
    <br>
    <p class="name">TVE10CS053</p>
    <p class="dept-name">
        Department of Computer Science <br><br>
        Aug 20, 2020
    </p>
</div>


# Question 1

## Aim
To implement and simulate algorithm for link state routing protocol.

## Theory
**Link-State Routing Protocols** are one of the two main classes of routing protocols used in packet switching networks for computer communications, the other being distance-vector routing protocols. Examples of link- state routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS). 

The link-state protocol is performed by every switching node in the network (i.e., nodes that are prepared
to forward packets; in the Internet, these are called routers). The basic concept of link-state routing is that
every node constructs a map of the connectivity to the network, in the form of a graph, showing which nodes
are connected to which other nodes. Each node then independently calculates the next best logical path from
it to every possible destination in the network. Each collection of best paths will then form each node’s routing
table.

## Algorith
```algorithm
START
   Step 1:  Take integer variable A
   Step 2:  Divide the variable A with (A-1 to 2)
   Step 3:  If A is divisible by any value (A-1 to 2) it is not prime
   Step 4:  Else it is prime
STOP
```

## code
```c
#include <stdio.h>

int main() {
   int i, number;
   int prime = 1;
   printf("\nEnter a number: ");
   scanf("%d", &number);

   for(i = 2; i < number; i++) {
      if((number % i) == 0) {
         prime = 0;
      }
   }
   if (number == 1)
      printf("1 is neither prime nor composite \n\n");
   else if (prime == 1)
      printf("%d is prime number.\n\n", number);
   else
      printf("%d is not a prime number\n\n.", number);
   return 0;
}
```
## Output

![alt text](demo.png "Title")

## Result
Implemented the program for simulating Link State Routing Protocol in c and was compiled using gcc and
executed in Ubuntu and the above output was obtained.

<br><br><br><br><br>
--------
# Question 2

## Aim
To implement and simulate algorithm for link state routing protocol.

## Theory
**Link-State Routing Protocols** are one of the two main classes of routing protocols used in packet switching networks for computer communications, the other being distance-vector routing protocols. Examples of link- state routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS). 

The link-state protocol is performed by every switching node in the network (i.e., nodes that are prepared
to forward packets; in the Internet, these are called routers). The basic concept of link-state routing is that
every node constructs a map of the connectivity to the network, in the form of a graph, showing which nodes
are connected to which other nodes. Each node then independently calculates the next best logical path from
it to every possible destination in the network. Each collection of best paths will then form each node’s routing
table.

## Algorith
```algorithm
START
   Step 1:  Take integer variable A
   Step 2:  Divide the variable A with (A-1 to 2)
   Step 3:  If A is divisible by any value (A-1 to 2) it is not prime
   Step 4:  Else it is prime
STOP
```

## code
```c
#include <stdio.h>

int main() {
   int i, number;
   int prime = 1;
   printf("\nEnter a number: ");
   scanf("%d", &number);

   for(i = 2; i < number; i++) {
      if((number % i) == 0) {
         prime = 0;
      }
   }
   if (number == 1)
      printf("1 is neither prime nor composite \n\n");
   else if (prime == 1)
      printf("%d is prime number.\n\n", number);
   else
      printf("%d is not a prime number\n\n.", number);
   return 0;
}
```
## Output

![alt text](demo.png "Title")

## Result
Implemented the program for simulating Link State Routing Protocol in c and was compiled using gcc and
executed in Ubuntu and the above output was obtained.
<br><br>
        """
    )
        f.close()
        return f"\n files created successfully at {os.getcwd()} \n"
    except FileExistsError:
        print('\n This file name already exist ..\n')
    

if __name__ == '__main__':
    fire.Fire()