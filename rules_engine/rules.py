class PreAssessment:
    def get_preassessment(balance_sheet, loan_amount):
        total_pl = 0
        total_av = 0
        avg_assetsValue = 0
        
        for bl in balance_sheet:
            total_pl += bl["profitOrLoss"]
            total_av += bl["assetsValue"]
        avg_assetsValue = int(total_av) / len(balance_sheet)
        print ("Average Asset Value", avg_assetsValue)
        
        if (avg_assetsValue > float(loan_amount)):
            preAssessment = 100
        elif (total_pl > int(loan_amount)):
            preAssessment = 60
        else:
            preAssessment = 20
            
        return preAssessment,avg_assetsValue

        
