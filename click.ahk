;click.ahk
; Simple script to repeatedly click at certain points
; Loops 1000 A_Times 
; Started by ctrl-alt-shift-q
; killed by `

^!+q::
Loop, 1000
{
	CoordMode, Mouse, Screen
	MouseMove, 147, 256
	Sleep, 1
	click, right
	MouseMove, 243, 359
	Sleep, 1
	click
	MouseMove, 259, 336
	Sleep, 1
	click
}
return

`::
    ExitApp
Return
