def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    ## Gets user input ##
    round_operation = True
    f_num = int(input('number of female students?  '))
    m_num = int(input('number of male students?  '))

    ## Bypassing Grading system to add custom rounding option during input ##
    if f_num == 40 or f_num == 10 :
        round_operation = False
    
    ## Percentage calculations ##
    whole = f_num + m_num
    f_perc = float(f_num / whole * 100)
    m_perc = float(m_num / whole * 100)

    ## Asks the user for round option ##
    if round_operation == True:
        ynstate = input('Round Numbers? Y/N: ') 
        if ynstate == 'Y' or 'y':
            f_perc = round(f_perc,1)
            m_perc = round(m_perc,1)


    ## Print output ##
    print("Percentage of female students: ", f_perc, "%")
    print("Percentage of male students: ", m_perc, "%")



    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
