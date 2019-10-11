function check()
		{
			var i=0, j="";
			str = document.getElementById("input").value
			str =str.split("-");
			var dob = new Date(str[2],str[1],str[0]);
            var today = new Date();
  			
  			var rs = today.getTime() - dob.getTime();
            rs = Math.floor(rs / (1000 * 60 * 60 * 24 * 365));
            document.getElementById("result").innerHTML = rs;

		}
