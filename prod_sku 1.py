from flask import Flask, request, jsonify
from db import query_db

app = Flask(__name__)

@app.route('/prod-sku', methods=['GET'])
def get_prod_sku():
    itemcode = request.args.get("itemcode")

    cols = """ItemCode, ItemName, FrgnName, ItmsGrpCod, CstGrpCode, VatGourpSa,
              CodeBars, VATLiable, PrchseItem, SellItem, InvntItem, IsCommited,
              OnOrder, IncomeAcct, ExmptIncom, MaxLevel, DfltWH, CardCode, SuppCatNum,
              BuyUnitMsr, NumInBuy, ReorderQty, MinLevel, LstEvlPric, LstEvlDate,
              LastPurPrc, LastPurCur, LastPurDat, ExitCur, ExitPrice, ExitWH, FirmCode,
              LstSalDate, CreateDate, UpdateDate, ExportCode, SalFactor1, PurFactor1,
              VatGroupPu, AvgPrice, PurPackMsr, SalPackMsr, validFor, validFrom, validTo,
              BlockOut, ObjType, ItemType, BaseUnit, CountryOrg, StockValue, IssueMthd,
              InvntryUom, PlaningSys, PrcrmntMtd, U_Category, U_Vendor, U_DisGrp, U_Product,
              U_StyleNo, U_Brand, U_Gender, U_ProdName, U_ProdType, U_Material, U_Sole,
              U_MRP, U_Remarks, U_UpdateTime"""

    sql = f"SELECT {cols} FROM OITM"
    params = []
    if itemcode:
        sql += " WHERE ItemCode = ?"
        params.append(itemcode)

    return jsonify(query_db(sql, params))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
