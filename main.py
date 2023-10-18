def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    f_num = int(input('number of female students?  '))
    m_num = int(input('number of male students?  '))
    whole = f_num + m_num 

    f_perc = float(f_num / whole * 100)
    m_perc = float(m_num / whole * 100)

    ynstate = input('Rounded Numbers? Y/N: ') 
    if ynstate == 'Y':
        f_perc = round(f_perc,1)
        m_perc = round(m_perc,1)

    
    f_perc = str(f_perc)
    m_perc = str(m_perc)


    print("Percentage of female students: " + f_perc + "%")
    print("Percentage of male students: " + m_perc + "%")



    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
