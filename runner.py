from pdfBillExtract.pbe import BillExtract
from pdfBillExtract import qrCards

qrCards.processClients(BillExtract().readPDFs())







