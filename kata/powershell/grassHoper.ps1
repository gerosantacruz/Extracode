function TerminalMove([int] $pos, [int] $roll) {
  # your code here
  return $pos + ($roll * 2)
}

write-output TeminalMove(3,6)