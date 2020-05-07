namespace DoubleEntry.Views
{
    partial class TransactionForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.accountTextBox = new System.Windows.Forms.TextBox();
            this.debitTextBox = new System.Windows.Forms.TextBox();
            this.creditTextBox = new System.Windows.Forms.TextBox();
            this.dataGridView = new System.Windows.Forms.DataGridView();
            this.addButton = new System.Windows.Forms.Button();
            this.addTransactionButton = new System.Windows.Forms.Button();
            this.dateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.date = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.account = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.debit = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.credit = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(10, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Fecha:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(158, 14);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(44, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Cuenta:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(10, 47);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(36, 13);
            this.label3.TabIndex = 1;
            this.label3.Text = "Debe:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(158, 47);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(39, 13);
            this.label4.TabIndex = 1;
            this.label4.Text = "Haber:";
            // 
            // accountTextBox
            // 
            this.accountTextBox.Location = new System.Drawing.Point(203, 11);
            this.accountTextBox.Name = "accountTextBox";
            this.accountTextBox.Size = new System.Drawing.Size(88, 20);
            this.accountTextBox.TabIndex = 1;
            // 
            // debitTextBox
            // 
            this.debitTextBox.Location = new System.Drawing.Point(52, 44);
            this.debitTextBox.Name = "debitTextBox";
            this.debitTextBox.Size = new System.Drawing.Size(90, 20);
            this.debitTextBox.TabIndex = 2;
            this.debitTextBox.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.debitTextBox_KeyPress);
            // 
            // creditTextBox
            // 
            this.creditTextBox.Location = new System.Drawing.Point(203, 44);
            this.creditTextBox.Name = "creditTextBox";
            this.creditTextBox.Size = new System.Drawing.Size(88, 20);
            this.creditTextBox.TabIndex = 3;
            // 
            // dataGridView
            // 
            this.dataGridView.AllowUserToAddRows = false;
            this.dataGridView.AllowUserToDeleteRows = false;
            this.dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.date,
            this.account,
            this.debit,
            this.credit});
            this.dataGridView.Location = new System.Drawing.Point(12, 80);
            this.dataGridView.Name = "dataGridView";
            this.dataGridView.ReadOnly = true;
            this.dataGridView.RowHeadersVisible = false;
            this.dataGridView.Size = new System.Drawing.Size(373, 234);
            this.dataGridView.TabIndex = 4;
            // 
            // addButton
            // 
            this.addButton.Location = new System.Drawing.Point(297, 42);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(88, 23);
            this.addButton.TabIndex = 4;
            this.addButton.Text = "Agregar";
            this.addButton.UseVisualStyleBackColor = true;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // addTransactionButton
            // 
            this.addTransactionButton.Location = new System.Drawing.Point(144, 328);
            this.addTransactionButton.Name = "addTransactionButton";
            this.addTransactionButton.Size = new System.Drawing.Size(104, 23);
            this.addTransactionButton.TabIndex = 5;
            this.addTransactionButton.Text = "Crear transacción";
            this.addTransactionButton.UseVisualStyleBackColor = true;
            this.addTransactionButton.Click += new System.EventHandler(this.addTransactionButton_Click);
            // 
            // dateTimePicker
            // 
            this.dateTimePicker.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.dateTimePicker.Location = new System.Drawing.Point(52, 13);
            this.dateTimePicker.Name = "dateTimePicker";
            this.dateTimePicker.Size = new System.Drawing.Size(90, 20);
            this.dateTimePicker.TabIndex = 0;
            // 
            // date
            // 
            this.date.HeaderText = "Fecha";
            this.date.Name = "date";
            this.date.ReadOnly = true;
            // 
            // account
            // 
            this.account.HeaderText = "Cuenta";
            this.account.Name = "account";
            this.account.ReadOnly = true;
            this.account.Width = 70;
            // 
            // debit
            // 
            this.debit.HeaderText = "Debe";
            this.debit.Name = "debit";
            this.debit.ReadOnly = true;
            // 
            // credit
            // 
            this.credit.HeaderText = "Haber";
            this.credit.Name = "credit";
            this.credit.ReadOnly = true;
            // 
            // TransactionForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(397, 363);
            this.Controls.Add(this.dateTimePicker);
            this.Controls.Add(this.addTransactionButton);
            this.Controls.Add(this.addButton);
            this.Controls.Add(this.dataGridView);
            this.Controls.Add(this.creditTextBox);
            this.Controls.Add(this.debitTextBox);
            this.Controls.Add(this.accountTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "TransactionForm";
            this.Text = "TransactionForm";
            this.Load += new System.EventHandler(this.TransactionForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox accountTextBox;
        private System.Windows.Forms.TextBox debitTextBox;
        private System.Windows.Forms.TextBox creditTextBox;
        private System.Windows.Forms.DataGridView dataGridView;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button addTransactionButton;
        private System.Windows.Forms.DateTimePicker dateTimePicker;
        private System.Windows.Forms.DataGridViewTextBoxColumn date;
        private System.Windows.Forms.DataGridViewTextBoxColumn account;
        private System.Windows.Forms.DataGridViewTextBoxColumn debit;
        private System.Windows.Forms.DataGridViewTextBoxColumn credit;
    }
}