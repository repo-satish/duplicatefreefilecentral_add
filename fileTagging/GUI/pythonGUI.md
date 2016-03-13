## Dialog Box with Simple Button-Sets
these boxes have a title, a message and predifined set of simple buttons like `Ok`, `Cancel`, `Abort`, `Retry`, `Ignore`, `Yes`, `No`, `Try_again` and `Continue`

```
import ctypes

ctypes.windll.user32.MessageBoxW(None, "body message", "dialogbox title", 0)
```

._______________________________________.
|numCode  |		button_set				|
+---------------------------------------+
|   0		Ok 							|
|   1		Ok, Cancel 					|
|   2		Abort, Retry, Ignore 		|
|   3		Yes, No, Cancel 			|
|   4		Yes, No 					|
|   5		Retry, Cancel 				|
|   6		Cancel, Try_again, Continue |
+---------------------------------------/______________
Table 1: Numeric Code for getting predifined ButtonSets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.___________________________.
|	button	|	returnValue |
+---------------------------+
|	Ok				1		|
|	Cancel			2		|
|	Abort			3		|
|	Retry			4		|
|	Ignore			5		|
|	Yes				6		|
|	No				7		|
|	Try_again		10		|
|	Continue		11		|
+---------------------------/__
Table 2: Button's return values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

> Note: pressing the red `X` close button returns value identical to `Cancel` button i.e. 2 **except** when `numCode==1` then `X` returns 1. Reason-- since the MessageBox has only one button `OK` so it is practically a notification and you can't canel_or_anything a notification, you have to just accept it, read it.
