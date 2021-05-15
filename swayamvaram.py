n  =Integer.parseInt(br.readLine())
a=n
boolean flag=true
String str=br.readLine()
String str1=br.readLine()
for(int i=0;i<n;i++)

    {

        flag=true;

        for(int j=0;j<a;j++)

        {

            if(str.charAt(i)==str1.charAt(0))

            {

               flag=false;

               str1=str1.substring(1,a);

               a--;

               break;

            }

            else

            {

               str1=str1.substring(1,a)+str1.substring(0,1);

            }

        }

            if(flag==true)

            {

               break;

            }

    }

        System.out.println(a);



