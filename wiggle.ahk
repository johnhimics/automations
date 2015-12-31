; wiggle.akh
; Wiggle the moust consistently so chat
; programs see that you are available

global min = 2 ;how many minutes between each wiggle
global wiggle = true ;variable to stop the wiggling

;ctrl-shift-w stops the wiggle
^+w::
wiggle := false
return

; ctrl-shift-alt-w enables wiggle
^!+w::
wiggle := true
loop {
	;ToolTip % wiggle
	sleep, % min*60*1000
	mousemove, 10, 0, 20, R
	mousemove, -10, 0, 20, R

	if (!wiggle) {
		;ToolTip "no-wiggle"
		return
	}
}
return
