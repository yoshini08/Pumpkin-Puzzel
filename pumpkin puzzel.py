print("Welcome To Pumpkin Puzzel..!!!")
print(
    ''' Jgy__
                            jWW  `""9Wf
                          _#WWW     IW
                         jWWWWW     IW
                 __,yyyyyWWWWW     IWyyyy___
            _jyWWP"^``"`.C"9*,J _.mqD:^^"WWWWWWQg__
          jgW"^.C/"    .C'     I    `D.     'D._"WQg_
        jWP` .C"       C'      I     `D._     `D._ "Qg_
      jQP`  .C    ,d^^b._      I      _.d^^b.   `D._ "Qg
     jQ^  .C"   /`   .+" \     I     / "+.   `\   `D.  XQ
    jQ'  .C'   |`  ."    )    _I    (     ".  |    `D.  4#
    Qf  .C     (   (    /    / /\    \     )  )     `D.  Qg
   jW   C'      \__\_.+'    / /  \    `+._/__/       `D  jQ
   Qf   C         C        /_/    \         D         D   Qk
   Qf   C      _  C        \_\____/         D  _      D   QF
   QL   C      \`+.__     _______     ______.+'/      D   QF
   B&   C.      \   \|    ||     |    ||      /       D   Qf
   jQ   `C.      \   |____|/     |____|/__   /      .D'   jW
    TQ   `C.      \._   `+.__________/___/|_/      .D'   jQ`
     9Q   `C.      C.`+._           |   |/.D'     .D'   jQ'
      "Qg  `C.     `C.   `"+-------'   ' .D'     .D'   pW`
       ^WQy `C.     `C.        I        .D'    _.D' yW"
         ^9Qy_`C.    `C.       I       .D'   _.D jgW"
            `9WQgC.__ `C.      I      .D'  _.Dp@@"`
           ilmk `""9WQQggyyyyyygyyyyyQggQWQH '''
)
print("Find the candies in pumpkin")
n=input("go left or right: ").lower()
if n=="left":
    print("you got a glowy eyes small pumpkin")
    a=input("what should we do now open or leave: ").lower()
    if a=='open':
        print("you got a clue and helping weapon to fight with ghosts")
        print("you have reached to a house which looks haunted go inside and search or no")
        b=input("enter search or no: ").lower()
        if b=='search':
            print("after entering you got to see 4 boxes")
            c=input("choose one box 'black' or 'red' or 'blue or 'pink' : ").lower()
            if c=='black':
                print("GAME OVER")
            elif c=='red':
                print(Someone else have taken your candies,GAME OVER")
            elif c=='blue':
                print("CONGRATS!!!YOU HAVE WON 50 CANDIES")
            elif c=='pink':
                print("CONGRATS!!YOU HAVE WON 1000 CANDIES")
            
        else :
            print("GAME OVER")
    else:
        print("There is a spooky ghost,Game Over")
else:
    print('''You have fell into a hole,
          GAME OVER''')
