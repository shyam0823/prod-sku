from flask import Flask, request, jsonify
from db import query_db

app = Flask(__name__)

@app.route('/spec-sku', methods=['GET'])
def get_spec_sku():
    itemcode = request.args.get("itemcode")

    # ✅ All columns from 02.Query Preview.xlsx
    cols = """ItemCode, ItemName, FrgnName, ItmsGrpCod, CstGrpCode, VatGourpSa,
              CodeBars, VATLiable, PrchseItem, SellItem, InvntItem, OnHand,
              IsCommited, OnOrder, IncomeAcct, ExmptIncom, MaxLevel, DfltWH,
              CardCode, SuppCatNum, BuyUnitMsr, NumInBuy, ReorderQty, MinLevel,
              LstEvlPric, LstEvlDate, LastPurPrc, LastPurCur, LastPurDat,
              ExitCur, ExitPrice, ExitWH, FirmCode, LstSalDate, CreateDate,
              UpdateDate, ExportCode, SalFactor1, PurFactor1, VatGroupPu, AvgPrice,
              PurPackMsr, SalPackMsr, validFor, validFrom, validTo, BlockOut,
              ObjType, ItemType, BaseUnit, CountryOrg, StockValue, IssueMthd,
              InvntryUom, PlaningSys, PrcrmntMtd, U_Colour, U_Category, U_SizeGrp,
              U_Size, U_Vendor, U_DisGrp, U_Product, U_StyleNo, U_Brand, U_Gender,
              U_ProdName, U_ProdType, U_Material, U_Sole, U_MRP, U_Remarks,
              U_UpdateTime"""

    sql = f"SELECT {cols} FROM OITM"
    params = []
    if itemcode:
        sql += " WHERE ItemCode = ?"
        params.append(itemcode)

    return jsonify(query_db(sql, params))

if __name__ == '__main__':
    app.run(port=5002, debug=True)
