
class FinancialStatements:
    """Mock service class for Request Balance Sheet"""    
    def BalanceSheet(company_name):
        print("Company name in FS ", company_name)
        """Create the shipment."""
        if company_name != 'Infosys':
            data = [
                {
                "year": 2022,
                "month": 1,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 2,
                "profitOrLoss": -2500,
                "assetsValue": 1234
                },
                {
                "year": 2022,
                "month": 3,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 4,
                "profitOrLoss": 250000,
                "assetsValue": 1234
                },
                            {
                "year": 2022,
                "month": 5,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 6,
                "profitOrLoss": 250000,
                "assetsValue": 1234
                },
                {
                "year": 2022,
                "month": 7,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 8,
                "profitOrLoss": 250000,
                "assetsValue": 1234
                },
                            {
                "year": 2022,
                "month": 9,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 10,
                "profitOrLoss": 250000,
                "assetsValue": 1234
                },
                {
                "year": 2022,
                "month": 11,
                "profitOrLoss": 240000,
                "assetsValue": 1244
                }, 
                {
                "year": 2022,
                "month": 12,
                "profitOrLoss": -2200,
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
    
    