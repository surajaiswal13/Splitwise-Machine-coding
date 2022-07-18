class BillController(object):

    def __init__(self, billService):
        self.billService = billService

    def addBill(self, id, groupId, amount, contribution, paidBy):
        return self.billService.addBill(id, groupId, amount, contribution, paidBy)  # Consider it as LinkedinUser, FacebookUser

    # Business Logic
    def getUserBalance(self, userId):
        balance = 0

        for billId in self.billService.billDetails:
            bill = self.billService.billDetails.get(billId)
            if userId in bill.getContribution():
                balance = balance - bill.getContribution().get(userId)

            if userId in bill.getPaidBy():
                balance = balance + bill.getPaidBy().get(userId)

        return balance

    def mostDebt(self, userController):
        
        most_debt_user = None
        most_debt = float('inf')

        for i in userController.userService.userDetails:
            # print(i)

            bal = self.getUserBalance(i)

            # most_debt = min(bal, most_debt)
            if bal < most_debt:
                most_debt = bal
                most_debt_user = i

        return [most_debt_user, most_debt]