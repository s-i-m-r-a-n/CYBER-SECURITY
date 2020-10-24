<?php
              if(isset($_POST["submit"]))
                           {
                                                       $servername = "localhost";
                                                       $username = "root";
                                                       $password = "";
                                                       $dbname = "database";
                                                       $name=$_POST["name"];
                                                       $age=$_POST["age"];
                                                       $pno=$_POST["pno"];
                                                       $conn=mysqli_connect($servername, $username, $password, $dbname);
                                                       if (!$conn)
                                                                    {
                                                                      die("Connection failed: " . mysqli_connect_error());
                                                                    }
                                                       $sql = "INSERT INTO data(name,age,pno)
                                                       VALUES ('$name',$age,$pno)";
                                                       if (mysqli_query($conn, $sql))
                                                                    {
                                                                      echo "New record created successfully";
                                                                    }
                                                       else
                                                                    {
                                                                      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
                                                                    }
                           }
?>

<html>
                           <body>
                           <form method="POST">
                                                       Name:<input type="text" name="name"><br>
                                                       Age:<input type="text" name="age"><br>
                                                       Phone Number:<input type="text" name="pno"><br><br>
                                                       <input type="submit" name="submit">
                           </form>
                           </body>

</html>
