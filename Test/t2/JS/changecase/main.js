function check()
		{
			var i=0, j="";
			str = document.getElementById("input").value
			for( i = 0; i < str.length; i++ )
			{
			if ((str.charAt(i)>="a" & str.charAt(i)<="z") | (str.charAt(i)>="A" & str.charAt(i)<="Z"))
				j+=(String.fromCharCode(str.charCodeAt(i)+1))
			else
				j+=String.fromCharCode(str.charCodeAt(i))
			}
			document.getElementById("result").innerHTML = j
			console.log(j)
		}
