import pandas as pd

df = pd.read_excel(r"C:\Users\Jeffrey\Desktop\notes\16th aug\Bankid.xlsx")
df['Combo'] = ""
# print(df)

target_account = pd.DataFrame(columns=['BankID', 'Account_type', 'Account_no'])
bank_error_records = pd.DataFrame(columns=['Seq_no', 'Record', 'Reason'])
filtered_account = pd.DataFrame(columns=['BankId', 'AccountNo'])

for a, row in df.iterrows():
    df['Combo'].loc[a] = (str(row.BankId) + str(row.AccountID))

# print(df)
accType = ('C', 'S', 'D')
for i, row in df.iterrows():
    if df['Combo'].duplicated().loc[i]:
        bank_error_records.loc[len(bank_error_records)] = [i, row.AccountID, "Duplicate entry"]
    elif len(str(row.AccountID))>=11:
        bank_error_records.loc[len(bank_error_records)] = [i, row.AccountID, "Incorrect acc number"]
    elif len(str(row.AccountID))<7:
        bank_error_records.loc[len(bank_error_records)] = [i, row.AccountID, "Incorrect acc number"]
    elif (str(row.AccountID)[0]) not in accType:
        bank_error_records.loc[len(bank_error_records)] = [i, row.AccountID, "Incorrect acc type"]
    else:
        filtered_account.loc[len(filtered_account)] = [row.BankId, row.AccountID]

filtered_account['join'] = ""

for b, row in filtered_account.iterrows():
    filtered_account['join'].loc[b] = (str(row.BankId) + str(row.AccountNo))

# print(filtered_account['join'])

for j in filtered_account['join']:
    if ('C' in j):
        b_id = j[0:5]
        # print("b_id", b_id)
        acc_id = j[5:]
        # print("acc_id", acc_id)
        if (acc_id[0] == 'C'):
            acc_type = 'Credit'
            acc = acc_id[1:]
            acc_no = acc
            target_account = target_account.append({'BankID': b_id, 'Account_type': acc_type, 'Account_no': acc_no}, ignore_index=True)

    elif ('D' in j):
        b_id = j[0:5]
        # print("b_id", b_id)
        acc_id = j[5:]
        # print("acc_id", acc_id)
        if (acc_id[0] == 'D'):
            acc_type = 'Debit'
            acc = acc_id[1:]
            acc_no = acc
            target_account = target_account.append({'BankID': b_id, 'Account_type': acc_type, 'Account_no': acc_no}, ignore_index=True)

    elif ('S' in j):
        b_id = j[0:5]
        # print("b_id", b_id)
        acc_id = j[5:]
        # print("acc_id", acc_id)
        if (acc_id[0] == 'S'):
            acc_type = 'Savings'
            acc = acc_id[1:]
            acc_no = acc
            target_account = target_account.append({'BankID': b_id, 'Account_type': acc_type, 'Account_no': acc_no}, ignore_index=True)

print(target_account)
print()
print(bank_error_records)

