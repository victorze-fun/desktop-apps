using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DoubleEntry.Views
{
    public partial class TransactionForm : Form
    {
        public TransactionForm()
        {
            InitializeComponent();
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            if (!ValidateEntry()) return;

            double debit = double.TryParse(debitTextBox.Text, out double deb) ? deb : 0;
            double credit = double.TryParse(creditTextBox.Text, out double cred) ? cred : 0;

            int n = dataGridView.Rows.Add();
            dataGridView.Rows[n].Cells[0].Value = dateTimePicker.Value.ToShortDateString();
            dataGridView.Rows[n].Cells[1].Value = accountTextBox.Text;
            dataGridView.Rows[n].Cells[2].Value = String.Format("{0:N2}", debit);
            dataGridView.Rows[n].Cells[3].Value = String.Format("{0:N2}", credit);

            CleanControls();
        }

        private bool ValidateEntry()
        {
            if (debitTextBox.Text != string.Empty && creditTextBox.Text != string.Empty)
            {
                MessageBox.Show("Si el campo Debe tiene un monto, el campo Haber debe estar vacio y viceversa.",
                    "Debe y Haber", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return false;
            }

            if ((debitTextBox.Text == string.Empty && creditTextBox.Text == string.Empty) || accountTextBox.Text == string.Empty)
            {
                MessageBox.Show("Los campos Cuenta, Debe y Haber no puden estar vacios",
                    "Campos vacios", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return false;
            }
            return true;
        }

        private void CleanControls()
        {
            accountTextBox.Clear();
            debitTextBox.Clear();
            creditTextBox.Clear();
        }

        private void DisableColumnSort()
        {
            foreach (DataGridViewColumn column in dataGridView.Columns)
            {
                column.SortMode = DataGridViewColumnSortMode.NotSortable;
            }
        }

        private void TransactionForm_Load(object sender, EventArgs e)
        {
            DisableColumnSort();
        }

        private void debitTextBox_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }

            // only allow one decimal point
            if ((e.KeyChar == '.') && ((sender as TextBox).Text.IndexOf('.') > -1))
            {
                e.Handled = true;
            }
        }

        private void addTransactionButton_Click(object sender, EventArgs e)
        {
            // TODO:
            // 1. Verifíca la partida doble.
        }
    }
}
