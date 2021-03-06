# Homework 3 Problem 1
# Programmer: Kyle Kloberdanz
# File: hw3p2.s

    .data
    x:          .float 3.0
    newLine:    .asciiz  "\n"

    .text

main:

    l.s $f2, x                      # loads variable x into $f2
    jal Exp                         # $f2 contains the argument, $f4 the return value

    jal PrintNewLine

    mov.s $f12, $f4                 # $f12, argument that will be printed
    jal PrintFloat

    jal PrintNewLine

Exit:
    li      $v0, 10                 # 10, syscall command to terminate
    syscall                         # End of program

#### This subroutine calculates the power ####
# Inputs: $f1: base
#         $t1: exponent
# Output: $f0: return value
# Other Registers used: $t3, $f12
Power:
    # $f1 contains the base
    # $t1 contains the exponent
    li      $t3, 0                      # $t3 will contain the increment
    li.s    $f0, 1.0                    # $f0 will contain the total

    PowerLoop:
        mul.s   $f0, $f0, $f1           # total = total * base
        addi    $t3, $t3, 1             # add 1 to increment
        blt     $t3, $t1, PowerLoop     # while exponent < increment

    jr $ra                              # subroutine finished, return

#### End of subroutine: Power ####

#### This suproutine calculates factorial ####
# Inputs: $a0: number to find factorial of
# Output: $v0: stores the return value
# Other Registers used: $sp 
Factorial:
    sub $sp, $sp, 8             # move stack pointer back by 8
    sw $ra, ($sp)               # save return address to stack
    sw $s0, 4($sp)              # save $s0 to position after $ra

    li $v0, 1                   
    beq $a0, $zero, FactorialFinished   # base case, if 0, then go through stack and multiply

    add  $s0, $a0, $zero         # $s0 will be saved
    sub  $a0, $a0, 1             # $a0 used as argument for recursive call
    jal Factorial

    mul $v0, $v0, $s0            # $v0 holds the final result

    FactorialFinished:
        lw $ra, ($sp)            # restores return address
        lw $s0, 4($sp)           # restores $s0
        addi $sp, $sp, 8         # repositions stack pointer

        jr $ra
#### End of subroutine: Factorial ####

### Calculate e^x using taylor series ###
# Inputs: $f2: holds value of x
# Output: $f4: holds value of e^x, return value
Exp:

    subu $sp, $sp, 4            # move stack pointer back by 4
    sw $ra, ($sp)               # save return address to stack


    li.s $f4, 1.0               # holds the total that will be returned
    li   $t0, 1                 # increment
    li   $t2, 10                # upperbound for increment



        whileLoop:



            mov.s  $f1, $f2                  # $f2 holds x, this will be passed as base to Power
            add $t1, $t0, $zero              # $t0 holds increment, this is passed as exponent to Power
            jal Power                        # $f0 will hold the return value


            mov.s $f12, $f0

            add $a0, $t0, $zero              # $t0 holds increment, this will be passed to Factorial
            jal Factorial                    # $v0 holds the return value


            mtc1 $v0, $f8                    # move the int in $v0 to $f8
            cvt.s.w $f8, $f8                 # convert the int in $f8 to a float
            div.s $f6, $f0, $f8              # divides $f0 by $f8, saved in $f6

            add.s $f4, $f4, $f6              # $f6 contains the result of power / factorial

            addi $t0, $t0, 1                 # i++
            blt  $t0, $t2, whileLoop         # while i < 10
    
    lw $ra, ($sp)                            # Restores return address
    addi $sp, $sp, 4                         # repositions stack pointer
    jr $ra                                   # Return to main

#########################################

### The Following are used for printing ###
# input: $a0: integer to print
# output: none
PrintInt:
    li      $v0, 1                  # 1, syscall command for print int; a0 holds int to print
    syscall

    jr $ra

# Input:  $f12: float to print
# output: none
PrintFloat:
    li      $v0, 2                  # 2, syscall for print float; $f12 holds float to print
    syscall
    
    jr $ra

# input: none
# output: none
PrintNewLine:
    li     $v0, 4                   # 4, syscall command for print string
    la     $a0, newLine
    syscall
    jr     $ra

# input: none
# output: none
PrintMessage:
    li $v0, 4
    la $a0, message
    syscall
    jr $ra
###########################################
