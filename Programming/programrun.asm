.MODEL SMALL
.DATA
    MAIN PROC
        MOV AH,2
        MOV DL,80
        SUB DL, 5
        INT 21H
        MOV DL, 70
        SUB DL, 3
        INT 21H
        MOV DL, 100
        SUB DL, 16
        INT 21H
        MOV DL, 100
        SUB DL, 30
        INT 21H
        MOV DL, 123
        INT 21H
        MOV DL, 75
        ADD DL, 50
        SUB DL, 60
        INT 21H
        MOV DL, 53
        INT 21H
        MOV DL, 53
        INT 21H
        MOV DL, 147
        SUB DL, 96
        INT 21H
        MOV DL, 80
        SUB DL, 3
        INT 21H
        MOV DL, 255
        MOV DH, 157
        SUB DL, DH
        INT 21H
        MOV DL, 255
        MOV DH, 147
        SUB DL, DH
        INT 21H
        MOV DH, 72
        MOV DL, 17
        ADD DL, DH
        INT 21H

        MOV DL, 130
        SUB DL, 5
        INT 21H


        MOV AH,4CH
        INT 21H

    MAIN ENDP
END MAIN