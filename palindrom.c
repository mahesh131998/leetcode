#include<stdio.h>


int reverse(long int x)
{
    long int temp;
    temp=0;
    while(x !=0)
    {
        temp= (temp*10)+(x%10);
        x= x/10;
    }
	return temp;

}
	
	


int isPalindrome(long int x)
{
	long int m;

	if(x<0)
	{	
		return 0;	
	}
	else if(x==0)
	{
		return 1;
	}
	else
	{
		m= reverse(x);
		if (m==x)
		{
			return 1;
		}
		else
		{
			return 0;
		}
}


}

void main()
{
	long int x;
	x=1021;
	long int y;
	y = isPalindrome(x);
	if(y==1)
	{
		printf(" True");
	}
	else{
		printf(" False");
	}
	
	printf(" %c ", y);
}


