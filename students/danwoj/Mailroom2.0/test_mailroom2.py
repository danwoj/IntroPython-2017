#!/usr/bin/env python3.6

import mailroom2, pytest

def test_db_query():
    qstate = "SELECT sql FROM sqlite_master ORDER BY tbl_name, type DESC, name"
    read_state = "SELECT * FROM don_list ORDER BY rowid DESC LIMIT 1;"
    write_state = "INSERT INTO don_list(don_fname, don_mi, don_lname, don_amt, don_date) VALUES ('Dan', 'NMN', 'Wojciechowski', 99999, '1 April 2017');"
    delete_state = "DELETE FROM don_list WHERE rowid = (SELECT MAX(rowid) FROM notes);"

    result = mailroom2.cmd_db(qstate)
    assert result == ('CREATE TABLE don_list(\n  "don_fname" TEXT,\n  "don_mi" TEXT,\n  "don_lname" TEXT,\n  "don_amt" TEXT,\n  "don_date" TEXT\n)',)

    result = mailroom2.cmd_db(read_state)
    assert result == ('Marcelle', 'R', 'Chmura', '48649', '31 August 2015')

    result2 = mailroom2.cmd_db(write_state)
    assert result2 == ('Dan', 'NMN', 'Wojciechowski', '99999', '1 April 2017')
    assert result != result2
    mailroom2(cmd_db(delete_state))
    result2 = mailroom2(cmd_db(read_state))
    assert result2 == result

#def test_add_name():
#    assert mailroom.add_name('Dan', 'Woj') is True

#def test_add_name2(capsys):
#    mailroom.add_name('Dan', 'Woj')
#    out, err = capsys.readouterr()
#    assert out == 'The name Dan Woj is not in the donor list. Adding them as a new donor.\n\n'

#def test_add_value():

#def test_print_letter():
#    assert mailroom.print_letter(4, 1234) is True

#def test_run_report(capfd):
#    mailroom.run_report()
#    out, err = capfd.readouterr()
#    assert out == '\n######################  Donor Report ######################\n\nDonor Name         | Total Given | Num Gifts | Average Gift\n-----------------------------------------------------------\nBill Gates         | $ 700.00    | 2         | $ 350.00\nMelvin Smith       | $ 8000.00   | 3         | $ 2666.67\nDaphnie Jones      | $ 2000.00   | 2         | $ 1000.00\nChauncey Doe       | $ 400.00    | 1         | $ 400.00\nFrieda Whatever    | $ 9000.00   | 3         | $ 3000.00\n'