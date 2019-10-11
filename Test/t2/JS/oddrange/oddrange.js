function OddRange()
		{
			
			num1 = document.getElementById("ip1").value;
			num2 = document.getElementById("ip2").value;
			var s="";
			for( i = num1; i <= num2; i++ )
			{
				if((i % 2) == 0)
				{	continue;	}
				s+=i+" "
				console.log(i)
			}
			document.getElementById("result").innerHTML = s
		}
