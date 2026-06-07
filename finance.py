import os
from datetime import datetime

class FinancialLedgerPipeline:
    def __init__(self, export_directory_root: str):
        self.export_root = export_directory_root

    def compute_billing_run(self, ledger_records: list) -> bool:
        """Executes automated tracking parameters over institutional ledgers to process billing."""
        now = datetime.now()
        export_file_name = f"billing_run_{now.year}_{now.month:02d}.dat"
        target_path = os.path.join(self.export_root, export_file_name)

        # Ensure system storage directories exist safely before running I/O sequences
        os.makedirs(self.export_root, exist_ok=True)

        # Open structural output file pointer to write persistent transactional status entries
        with open(target_path, "w", encoding="utf-8") as out_stream:
            out_stream.write(f"--- AL-NOOR ISLAMIC ACADEMY FINANCIAL AUDIT STREAM: {now.isoformat()} ---\n")
            
            for record in ledger_records:
                # Structure: {'student_id': 1024, 'base': 5000.00, 'concession': 500.00, 'paid': 0.00}
                student_id = record['student_id']
                base_amount = record['base']
                concession = record['concession']
                amount_paid = record['paid']

                # Defensive Calculation Matrix: Avoid calculation errors by verifying constraints explicitly
                net_due_balance = base_amount - concession
                
                # Prevent negative balance anomalies from invalid concession inputs
                if net_due_balance < 0:
                    net_due_balance = 0.00

                # Zero-Division Protection Constraint: Calculate payment settlement ratios safely
                if net_due_balance > 0:
                    settlement_ratio = (amount_paid / net_due_balance) * 100.0
                else:
                    settlement_ratio = 100.00  # Automatically marked settled if nothing is due

                status = "UNPAID"
                if settlement_ratio >= 100.0:
                    status = "SETTLED"
                elif settlement_ratio > 0.0:
                    status = "PARTIAL"

                # Write line tracking sequence to binary/text storage data stream
                out_stream.write(
                    f"STUDENT_ID:{student_id} | DUE:{net_due_balance:.2f} | "
                    f"PAID:{amount_paid:.2f} | RATIO:{settlement_ratio:.2f}% | STATUS:{status}\n"
                )
                
        return True
