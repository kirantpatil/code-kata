class Decision:
  def check_status(company_name, preassessment, balance_sheet):
          print("Preassessment value is ", preassessment)
          if (preassessment == 100):
            return "Loan approved 100% of the requested value"
          elif (preassessment == 60):
            return "Loan approved 60% of the requested value"
          else:
            return "Loan approved 20% of the requested value"