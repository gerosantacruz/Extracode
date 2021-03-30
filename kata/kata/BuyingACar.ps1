function nb-months
{
    [OutputType([string])]
    Param ([int]$startPriceOld, [int]$startPriceNew, [int]$savingperMonth, [double]$percentLossByMonth)

    # your code
    $month = 0
    [Double] $saving = 0
    if ($startPriceOld -ge $startPriceNew){
        return @(0, ($startPriceOld - $startPriceNew)) -join ","
    }

    while (($startPriceOld + $saving) -le $startPriceNew) {
                 
        $month++

        if($month % 2 -eq 0 ){ $percentLossByMonth += 0.5}

        [Double] $startPriceOld = $startPriceOld - ($startPriceOld * $percentLossByMonth/100)
        [Double] $startPriceNew = $startPriceNew - ($startPriceNew * $percentLossByMonth/100)
        $saving += $savingperMonth 
           
    }
    
    return $month, [Math]::Round((($startPriceOld + $saving) - $startPriceNew)) -join ","
}

write-output (nb-months 2000.0 8000.0 1000.0 1.5)


#Kata from CodeWars in powershell https://www.codewars.com/kata/554a44516729e4d80b000012/train/powershell

