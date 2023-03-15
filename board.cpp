#include <iostream>
using namespace std;

int main()
{
    int x[19][11];
    int i=0;
    int j=0;
    for(i=0;i<19;i++)
    {
        for(j=0;j<11;j++)
        {
            x[i][j]=0;
        }
    }

    for(i=0;i<19;i=i+2)
    {
        x[i][4]=1;
        x[i][6]=1;
    }
    for(i=2;i<17;i=i+2)
    {
        x[i][2]=1;
        x[i][8]=1;
    }
    for(i=6;i<13;i=i+2)
    {
        x[i][0]=1;
        x[i][10]=1;
    }
    for(i=1;i<18;i=i+2)
    {
        x[i][3]=1;
        x[i][5]=1;
        x[i][7]=1;
    }
    for(i=3;i<16;i=i+2)
    {
        x[i][1]=1;
        x[i][9]=1;
    }

    printf("\n");
    for(i=0;i<19;i++)
    {
        for(j=0;j<11;j++)
        {
            printf("%d",x[i][j]);
            printf("\t");
        }
        printf("\n");
    }

    /*check dir: u,d,ul,ur,dl,dr*/
}
