<?php
 
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "database";
    $conn=mysqli_connect($servername, $username, $password, $dbname);
    if (!$conn) 
     {
       die("Connection failed: " . mysqli_connect_error());
     }
    $sql = "select * from data";
    if($result=$conn->query($sql))
     {
      if($result->num_rows>0) 
       {
        while($row=$result->fetch_assoc())
         {
          $data[] =$row;
         }
       }
     }
  
?> 
<html>
  <body>
    <?php 
      foreach($data as $d)
       {
        ?>
          Name:<?=$d["name"]?>
          Age:<?=$d["age"]?>
          Phone number<?=$d["pno"]?>
        <?php
       }
    ?>
  </body>
</html
