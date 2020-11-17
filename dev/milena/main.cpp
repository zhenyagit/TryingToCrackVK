
#include <iostream>
#include <fstream>
#include <cmath>
#include <float.h>
using namespace std;

double f(double x, double a[5])
{
	return a[0] + a[1] / x + a[2] * x + a[3] * x * x + a[4] * x * x * x;
}
double function_root(double x, double a[5], double roots[], int quinpargtity)
{
	int i = 0;
	double newf = f(x,a);
	while (i < quinpargtity)
	{
		newf = newf*(1 / (x - roots[i]));
		i++;
	}
	return (newf);
}
int main()
{
	double inparg[5];
	double roots[5];
	double a, b, epsilon, delta, ab, bb;
	bool doubche = 0;
	ofstream fout;
	fout.open("output.txt");

	cout << "Enter a0, a1, a2, a3" << endl;
	cin >> inparg[0] >> inparg[1] >> inparg[2] >> inparg[3] >> inparg[4];
	cout << "Enter a,b" << endl;
	cin >> ab >> bb;
	cout << "Enter epsilon" << endl;
	cin >> epsilon;
	fout << "F(x) = (" << inparg[0] << ")+(" << inparg[1] << ")/x+(" << inparg[2] << ")x+(" << inparg[3] << ")x^2+(" << inparg[4] << ")x^3" << endl;
	fout << "Epsilon = " << epsilon << endl;
	fout << "a = " << ab << "; b = " << bb << ";" << endl;

	int i= 0;
	
	while (i < 4)
	{
		a = ab;
		b = bb;
		// cout << a << "  " << b << endl;
		while (abs(b - a) > epsilon)
		{
			delta = (a + b) / 2.0;
			if (function_root(a, inparg,roots,i)*function_root(delta, inparg,roots,i) < 0) b = delta;
			if (function_root(b, inparg,roots,i)*function_root(delta, inparg,roots,i) < 0) a = delta;
			if ((function_root(b, inparg,roots,i)*function_root(delta, inparg,roots,i) > 0) && (function_root(a, inparg,roots,i)*function_root(delta, inparg,roots,i) > 0))
			{
				if (doubche) 
				{
					b -= epsilon;
					doubche = 0;
				}
				else
				{
					a += epsilon;
					doubche = 1;
				}
			}
		}
		if (function_root(b, inparg,roots,i)*function_root(a, inparg,roots,i) > 0) break;
		if ((a*b < 0) ) bb = delta - epsilon;
		else 
		{
			roots[i] = delta;
			i++;
			if (delta > 0) bb = delta - epsilon;
			else ab = delta + epsilon;
		}
		
	}
	cout << "Quantity of roots:" << i << endl;
	fout << "Quantity of roots:" << i << endl;
	int k = 0;
	while (k<i)
	{
		cout <<"Root number " << k << " = " << roots[k] << endl;
		fout <<"Root number " << k << " = " << roots[k] << endl;
		k = k+1;	
	}
	fout.close();
	cin >> k;
	return 0;
}


