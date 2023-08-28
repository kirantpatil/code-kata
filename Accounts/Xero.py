
class FinancialStatements:
    """Mock service class for Request Balance Sheet"""    
    def BalanceSheet(company_name):
        print("Company name in FS ", company_name)
        """Create the shipment."""
        if company_name != 'Infosys':
            data = [
                {
                "year": 2020,
                "month": 11,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2020,
                "month": 12,
                "profitOrLoss": 250000,
                "assetsValue": 1234
                }
            ]
        else:
            data = [
                {
                "year": 2020,
                "month": 9,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }
            ]
        return (data)
    
    