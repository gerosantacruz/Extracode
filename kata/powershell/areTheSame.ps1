$num =  121, 144, 19, 161, 19, 1434, 119, 11 
$pow =  14641, 20736, 361, 25921, 361, 20736, 361, 121 

function comp($a1, $a2)
{
    if ($a1.Length -ne $a2.Length) {
        return $false
      }

      if ($a1.Length -eq $null) {
        return $false
      }

      if ($a2.Length -eq $null) {
        return $false
      }



    $elevate = @()
    foreach($i in $a1){
            $elevate += [Math]::Pow($i,2)
    }

    (($elevate | Sort-Object) -join ' ') -eq (($a2|Sort-Object) -join ' ')
    

    

}


comp -a1 $num -a2 $pow