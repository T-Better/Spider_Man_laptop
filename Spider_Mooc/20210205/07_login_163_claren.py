import requests


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "cookie":"mail_upx_nf=; mail_idc=""; secu_info=1; locale=; face=js6; mail_uid=m15132352140_1@163.com; mail_style=js6; mail_host=mail.163.com; _ntes_nnid=3dec55b9ca3e9ef70bd05294d103ac0d,1612270627061; _ntes_nuid=3dec55b9ca3e9ef70bd05294d103ac0d; starttime=; ntes_misc=0||10#0|0|000020|0|mail163||0; nts_mail_user=15132352140@163.com:-1:1; df=mail163_letter; mail_psc_fingerprint=68d5d3987e2bfaf4e847cfae3450ae08; NTES_SESS=aM6xP7HTxdBLUTtc2nxL9POxC1xife8MRJ3VJthNcktkd3GbdnHABwp.a1zrejVnQqKJeULn2pVd1W9FKc2NsA1IkdOsumkP1zfoDqYpdJr4iXeCIjmyh.CdyzEbN._zIRKIZNEB_Dr264HKQanb0evCWu1_rcibU6T4LgPiDQ2xmXo6YEfkrKlvVf9yNGerRCIzu1GS_QJyI4kxa8pWz1szD4f2DoE8t; S_INFO=1612271155|0|1&65##|m15132352140_1#claren_lau; P_INFO=m15132352140_1@163.com|1612271155|0|mail163|00&99|bej&1612270831&mail163#bej&null#10#0#0|151140&1|mail163&cc|15132352140@163.com; mail_upx=c5bj.mail.163.com|c6bj.mail.163.com|c7bj.mail.163.com|c1bj.mail.163.com|c2bj.mail.163.com|c3bj.mail.163.com|c4bj.mail.163.com; Coremail=17b7e478851fd%mCpAlNPVrcLnyqlibcVVOcHfaGbceHii%g1a122.mail.163.com; cm_last_info=dT1tMTUxMzIzNTIxNDBfMSU0MDE2My5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEbUNwQWxOUFZyY0xueXFsaWJjVlZPY0hmYUdiY2VIaWkmcz1tQ3BBbE5QVnJjTG55cWxpYmNWVk9jSGZhR2JjZUhpaSZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RtQ3BBbE5QVnJjTG55cWxpYmNWVk9jSGZhR2JjZUhpaSZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJmw9LTEmdD0tMSZhcz10cnVl; MAIL_SESS=aM6xP7HTxdBLUTtc2nxL9POxC1xife8MRJ3VJthNcktkd3GbdnHABwp.a1zrejVnQqKJeULn2pVd1W9FKc2NsA1IkdOsumkP1zfoDqYpdJr4iXeCIjmyh.CdyzEbN._zIRKIZNEB_Dr264HKQanb0evCWu1_rcibU6T4LgPiDQ2xmXo6YEfkrKlvVf9yNGerRCIzu1GS_QJyI4kxa8pWz1szD4f2DoE8t; MAIL_SINFO=1612271155|0|1&65##|m15132352140_1#claren_lau; MAIL_PINFO=m15132352140_1@163.com|1612271155|0|mail163|00&99|bej&1612270831&mail163#bej&null#10#0#0|151140&1|mail163&cc|15132352140@163.com; mail_entry_sess=2e475f0f35676abbcf1080473d4d4a642fad5b5f0853c9d38b524b7c1c8335ff0142cca5026a115fa883e8eadeb93ed93fa663441fa31a91b51ff07c740460ea1b71a9f2eace9eccb02fb4080a2b14414f0e7be0ef24a8a616e7e2ae8bb6bac1b5d640955568d8c25db1c3168469d004435c5f90791819f6cc9a62ca5c6fe1d481a60376c539d6f3c046ca493c0dc3979060f242cecd5d94a6589dde05d064471ab8eddf3291d10f660903f7dcbc92a441c7575ed776775fc9e1a8bab2bfff0b; Coremail.sid=mCpAlNPVrcLnyqlibcVVOcHfaGbceHii; JSESSIONID=41D0582527BAF6E63A77EA507227A5DE"
}

r = requests.post("https://mail.163.com/js6/s?sid=mCpAlNPVrcLnyqlibcVVOcHfaGbceHii&func=mbox:listMessages",headers=headers)

with open("151_163mail0202_03.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())