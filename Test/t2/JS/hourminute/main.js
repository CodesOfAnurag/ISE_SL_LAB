function check()
		{
			var i=0, j="";
			total = parseInt(document.getElementById("input").value)
			var hr=parseInt(total/60)
			var min=parseInt(total%60)
			document.getElementById("result").innerHTML = hr+":"+min
		}
