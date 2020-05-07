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
    public partial class DayBookForm : Form
    {
        public DayBookForm()
        {
            InitializeComponent();
        }

        private void DayBookForm_Load(object sender, EventArgs e)
        {
            foreach (DataGridViewColumn column in dataGridView.Columns)
            {
                column.SortMode = DataGridViewColumnSortMode.NotSortable;
            }

            int n = dataGridView.Rows.Add();
            dataGridView.Rows[n].Cells[0].Value = "1";
            dataGridView.Rows[n].Cells[1].Value = "10/12/2020";
            dataGridView.Rows[n].Cells[2].Value = "10";
            dataGridView.Rows[n].Cells[3].Value = "10,000";
            dataGridView.Rows[n].Cells[4].Value = "";

            n = dataGridView.Rows.Add();
            dataGridView.Rows[n].Cells[0].Value = "1";
            dataGridView.Rows[n].Cells[1].Value = "10/12/2020";
            dataGridView.Rows[n].Cells[2].Value = "12";
            dataGridView.Rows[n].Cells[3].Value = "0";
            dataGridView.Rows[n].Cells[4].Value = "10,000";
        }

        private void transactionButton_Click(object sender, EventArgs e)
        {
            var transactionFrom = new TransactionForm();
            AddOwnedForm(transactionFrom);
            transactionFrom.ShowDialog();
        }
    }
}
