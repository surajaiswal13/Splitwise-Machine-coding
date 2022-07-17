from splitwise.services.bill_service_interface import BillServiceInterface
from splitwise.models.bill import Bill

class BillService(BillServiceInterface):
    billDetails = {}
    def addBill(self, id, groupId, amount, contribution, paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(id)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)

        self.__class__.billDetails[id] = bill # It is a class Level Dictionary not object level

        return bill