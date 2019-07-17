# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from _datetime import datetime




def send_newsletter(userName,userEmail,publications):


    desc1 = publications[0][1]
    if desc1 is None:
        desc1 = 'no description'
    desc2 = publications[1][1]
    if desc2 is None:
        desc2 = 'no description'
    desc3 = publications[2][1]
    if desc3 is None:
        desc3 = 'no description'
    # verifiez que les dates sont pas nulle !

    date1 = publications[0][2]
    print(date1)
    if date1 is None:
        date1 = datetime.datetime.today().strftime('%Y-%m-%d')
    else :
        date1 = publications[0][2].strftime('%Y-%m-%d')

    date2 = publications[1][2]
    if date2 is None:
        date2 = datetime.datetime.today().strftime('%Y-%m-%d')
    else:
        date2 = publications[1][2].strftime('%Y-%m-%d')

    date3 = publications[2][2].strftime('%Y-%m-%d')
    if date3 is None:
        date3 = datetime.datetime.today().strftime('%Y-%m-%d')

    img1 = publications[0][3]
    if img1 is None:
        img1 = 'https://gianyarkab.bps.go.id/backend/fileMenu/Logo-singkat-SP2020.png?fbclid=IwAR05-TXJfampRegxFwhaz2JNGe9j8ELkIibKYEgsGi_zYDBowPHBdHLsM-Y'
    img2 = publications[1][3]
    if img2 is None:
        img2 = 'https://gianyarkab.bps.go.id/backend/fileMenu/Logo-singkat-SP2020.png?fbclid=IwAR05-TXJfampRegxFwhaz2JNGe9j8ELkIibKYEgsGi_zYDBowPHBdHLsM-Y'
    img3 = publications[2][3]
    if img3 is None:
        img3 = 'https://gianyarkab.bps.go.id/backend/fileMenu/Logo-singkat-SP2020.png?fbclid=IwAR05-TXJfampRegxFwhaz2JNGe9j8ELkIibKYEgsGi_zYDBowPHBdHLsM-Y'


    title1 = publications[0][5]
    if title1 is None:
        title1 = 'Untitled'
    title2 = publications[1][5]
    if title2 is None:
        title2 = 'Untitled'
    title3 = publications[2][5]
    if title3 is None:
        title3 = 'Untitled'

    download_link1 = publications[0][7]
    if download_link1 is None :
        download_link1 ='nolink'
    download_link2 = publications[1][7]
    if download_link2 is None :
        download_link2 ='nolink'
    download_link3 = publications[2][7]
    if download_link3 is None :
        download_link3 ='nolink'

    full_link1= publications[0][6]
    if full_link1 is None :
        full_link1 = 'nolink'
    full_link2 = publications[1][6]
    if full_link2 is None :
        full_link2 = 'nolink'
    full_link3 = publications[2][6]
    if full_link3 is None :
        full_link3 = 'nolink'


    msg = MIMEMultipart()
    newsletterAdress = 'gianyarkab.newsletter@gmail.com'
    newsletterPassword = 'stikom2019'
    recipientAdress = userEmail
    msg['From'] = newsletterAdress
    msg['To'] = recipientAdress
    msg['Subject'] = 'GianyarKab Newsletter'

    html = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="format-detection" content="date=no" />
        <meta name="format-detection" content="address=no" />
        <meta name="format-detection" content="telephone=no" />
        <meta name="x-apple-disable-message-reformatting" />
        <!--[if !mso]><!-->
        <link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i" rel="stylesheet" />
        <!--<![endif]-->
        <title>Email Template</title>
        <!--[if gte mso 9]>
        <style type="text/css" media="all">
            sup { font-size: 100% !important; }
        </style>
        <![endif]-->


        <style type="text/css" media="screen">
            /* Linked Styles */
            body { padding:0 !important; margin:0 !important; display:block !important; min-width:100% !important; width:100% !important; background:#f3f4f6; -webkit-text-size-adjust:none }
            a { color:#000001; text-decoration:none }
            p { padding:0 !important; margin:0 !important }
            img { -ms-interpolation-mode: bicubic; /* Allow smoother rendering of resized image in Internet Explorer */ }
            .mcnPreviewText { display: none !important; }


            /* Mobile styles */
            @media only screen and (max-device-width: 480px), only screen and (max-width: 480px) {
                .mobile-shell { width: 100% !important; min-width: 100% !important; }
                .bg { background-size: 100% auto !important; -webkit-background-size: 100% auto !important; }

                .text-header,
                .m-center { text-align: center !important; }

                .center { margin: 0 auto !important; }
                .container { padding: 20px 10px !important }

                .td { width: 100% !important; min-width: 100% !important; }

                .m-br-15 { height: 15px !important; }
                .p30-15 { padding: 30px 15px !important; }
                .p0-15-30 { padding: 0px 15px 30px 15px !important; }
                .mpb30 { padding-bottom: 30px !important; }

                .m-td,
                .m-hide { display: none !important; width: 0 !important; height: 0 !important; font-size: 0 !important; line-height: 0 !important; min-height: 0 !important; }

                .m-block { display: block !important; }

                .fluid-img img { width: 100% !important; max-width: 100% !important; height: auto !important; }

                .column,
                .column-dir,
                .column-top,
                .column-empty,
                .column-empty2,
                .column-dir-top { float: left !important; width: 100% !important; display: block !important; }

                .column-empty { padding-bottom: 30px !important; }
                .column-empty2 { padding-bottom: 10px !important; }

                .content-spacing { width: 15px !important; }
            }
        </style>
    </head>
    <body class="body" style="padding:0 !important; margin:0 !important; display:block !important; min-width:100% !important; width:100% !important; background:#f3f4f6; -webkit-text-size-adjust:none;">
        <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f3f4f6">
            <tr>
                <td align="center" valign="top">
                    <table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
                        <tr>
                            <td class="td container" style="width:650px; min-width:650px; font-size:0pt; line-height:0pt; margin:0; font-weight:normal; padding:55px 0px;">
                                <!-- Header -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td class="p30-15 tbrr" style="padding: 30px; border-radius:26px 26px 0px 0px;" bgcolor="#ffffff">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <th class="column" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <td class="text-header" style="color:#999999; font-family:'Playfair Display', Georgia,serif; font-size:13px; line-height:18px; text-align:right;"><a href="#" target="_blank" class="link2" style="color:#999999; text-decoration:none;"><span class="link2" style="color:#999999; text-decoration:none;"> Welcome """ + userName + """</span></a></td>
                                                            </tr>
                                                        </table>
                                                    </th>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <!-- END Header -->



                                <!-- Intro -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                                    <tr>
                                        <td style="padding-bottom: 10px;">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td class="p30-15" style="padding: 60px 30px;">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <td class="h1 pb25" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:40px; line-height:46px; text-align:center; padding-bottom:25px;">Badan Pusat Statistik Kabupaten Gianyar</td>
                                                            </tr>
                                                            <tr>
                                                                <td class="text-center pb25" style="color:#666666; font-family:'Muli', Arial,sans-serif; font-size:16px; line-height:30px; text-align:center; padding-bottom:25px;"> Badan Pusat Statistik (BPS-Statistics Indonesia) is a Non-Departmental Government Institution directly responsible to the President.  <span class="m-hide"><br /></span></td>
                                                            </tr>
                                                            <!-- Button -->
                                                            <tr>
                                                                <td align="center">
                                                                    <table class="center" border="0" cellspacing="0" cellpadding="0" style="text-align:center;">
                                                                        <tr>
                                                                            <td class="text-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; padding:12px 30px; text-align:center; border-radius:25px; text-transform:uppercase;"><a href="https://gianyarkab.bps.go.id/" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">CLICK HERE</span></a></td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <!-- END Button -->
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <!-- END Intro -->



                                <!-- Three Articles / IMage On The edge -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td style="padding: 0px 30px 50px 30px;" class="p0-15-30" bgcolor="#ffffff">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td style="padding-bottom: 40px;" class="mpb30">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <td class="content-spacing" width="210" style="font-size:0pt; line-height:0pt; text-align:left;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#d9dada" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;"><tr><td bgcolor="#d9dada" height="1" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;">&nbsp;</td></tr></table>
    </td>
                                                                <td class="section-title" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:16px; line-height:22px; text-align:center; text-transform:uppercase;">Your Own Newsletter</td>
                                                                <td class="content-spacing" width="210" style="font-size:0pt; line-height:0pt; text-align:left;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#d9dada" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;"><tr><td bgcolor="#d9dada" height="1" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;">&nbsp;</td></tr></table>
    </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <!-- FIRST ARTICLE -->
                                                <tr>

                                                    <td style="padding-bottom: 10px;">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <th class="column-top" width="290" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <!-- FIRST IMAGE -->
                                                                        <tr>
                                                                            <td class="fluid-img" style="font-size:0pt; line-height:0pt; text-align:left;"><img src="""+img1+""" width="290" height="290" border="0" alt="" /></td>
                                                                        </tr>
                                                                    </table>
                                                                </th>
                                                                <th class="column-empty" width="30" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"></th>
                                                                <th class="column" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                        <tr>
                                                                            <td class="h4 pb20" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:20px; line-height:28px; text-align:left; padding-bottom:20px;">
                                                                                """+date1+' : '+title1+"""
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td class="text pb20" style="color:#999999; font-family:Arial,sans-serif; font-size:14px; line-height:26px; text-align:left; padding-bottom:20px;">
                                                                                """ + desc1 +"""
                                                                            </td>
                                                                        </tr>
                                                                        <!-- Button -->
                                                                        <tr>
                                                                            <td align="left" class="mpb30">
                                                                                <table border="0" cellspacing="0" cellpadding="0">
                                                                                    <tr>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+full_link1+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">SEE MORE</span></a></td>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+download_link1+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">DOWNLOAD</span></a></td>
                                                                                    
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                        <!-- END Button -->
                                                                    </table>
                                                                </th>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <!-- END FIRST ARTICLE -->

                                                <!-- SECOND ARTICLE -->
                                                <tr>
                                                    <td style="padding-bottom: 10px;">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" dir="rtl" style="direction: rtl;">
                                                            <tr>
                                                                <th class="column-dir-top" dir="ltr" width="290" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; direction:ltr; vertical-align:top;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <!-- SECOND IMAGE -->
                                                                        <tr>
                                                                            <td class="fluid-img" style="font-size:0pt; line-height:0pt; text-align:left;"><img src="""+img2+""" width="290" height="290" border="0" alt="" /></td>
                                                                        </tr>
                                                                    </table>
                                                                </th>
                                                                <th class="column-empty" width="30" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"></th>
                                                                <th class="column-dir" dir="ltr" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; direction:ltr;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                        <tr>
                                                                            <td class="h4 pb20" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:20px; line-height:28px; text-align:left; padding-bottom:20px;">
                                                                                """+date2+' : '+title2+"""
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td class="text pb20" style="color:#999999; font-family:Arial,sans-serif; font-size:14px; line-height:26px; text-align:left; padding-bottom:20px;">
                                                                                """ + desc2 + """
                                                                            </td>
                                                                        </tr>
                                                                        <!-- Button -->
                                                                        <tr>
                                                                            <td align="left" class="mpb30">
                                                                                <table border="0" cellspacing="0" cellpadding="0">
                                                                                    <tr>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+full_link2+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">SEE MORE</span></a></td>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+download_link2+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">DOWNLOAD</span></a></td>
                                                                                    
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                        <!-- END Button -->
                                                                    </table>
                                                                </th>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <!-- END SECOND ARTICLE -->

                                                <!-- THIRD ARTICLE -->
                                                <tr>
                                                    <td style="padding-bottom: 10px;">
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <th class="column-top" width="290" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <!-- THIRD IMAGE -->
                                                                        <tr>
                                                                            <td class="fluid-img" style="font-size:0pt; line-height:0pt; text-align:left;"><img src="""+img3+""" width="290" height="290" border="0" alt="" /></td>
                                                                        </tr>
                                                                    </table>
                                                                </th>
                                                                <th class="column-empty" width="30" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"></th>
                                                                <th class="column" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                        <tr>
                                                                            <td class="h4 pb20" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:20px; line-height:28px; text-align:left; padding-bottom:20px;">
                                                                                """+date3+' : '+title3+"""
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td class="text pb20" style="color:#999999; font-family:Arial,sans-serif; font-size:14px; line-height:26px; text-align:left; padding-bottom:20px;">
                                                                                """ + desc3 + """
                                                                            </td>
                                                                        </tr>
                                                                        <!-- Button -->
                                                                        <tr>
                                                                            <td align="left">
                                                                                <table border="0" cellspacing="0" cellpadding="0">
                                                                                    <tr>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+full_link3+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">SEE MORE</span></a></td>
                                                                                        <td class="text-button yellow-border-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; text-align:center; border-radius:25px; text-transform:uppercase; background-color:transparent; border:2px solid #fecc7b; padding:12px 40px;"><a href="""+download_link3+""" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">DOWNLOAD</span></a></td>
                                                                                    
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                        <!-- END Button -->
                                                                    </table>
                                                                </th>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <!-- END THIRD ARTICLE -->




                                <!-- CTA -->
                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td style="padding: 0px 30px 50px 30px;" class="p0-15-30" bgcolor="#ffffff">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td style="padding-bottom: 40px;" class="mpb30" >
                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                            <tr>
                                                                <td class="content-spacing" width="210" style="font-size:0pt; line-height:0pt; text-align:left;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#d9dada" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;"><tr><td bgcolor="#d9dada" height="1" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;">&nbsp;</td></tr></table>
    </td>
                                                                <td class="section-title" style="border: 1px solid #d9dada; border-radius: 20px; padding: 5px; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:16px; line-height:22px; text-align:center; text-transform:uppercase;">HELP</td>
                                                                <td class="content-spacing" width="210" style="font-size:0pt; line-height:0pt; text-align:left;"><table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#d9dada" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;"><tr><td bgcolor="#d9dada" height="1" class="border" style="font-size:0pt; line-height:0pt; text-align:center; width:100%; min-width:100%;">&nbsp;</td></tr></table>
    </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="h2 pb30" style="color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:30px; line-height:36px; text-align:center; padding-bottom:30px;">
                                                        Newsletter doesn't work good for you ? Contact us !
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center pb30" style="color:#666666; font-family:'Muli', Arial,sans-serif; font-size:16px; line-height:30px; text-align:center; padding-bottom:30px;">
                                                        Badan Pusat Statistik Kabupaten Gianyar JlErlangga Nomor 5, Gianyar 80511, Telp (0361) 943075 Faks (0361) 943075, Mailbox : bps5104@bps.go.id <span class="m-hide">
                                                    </td>
                                                </tr>
                                                <!-- Button -->
                                                <tr>
                                                    <td align="center">
                                                        <table class="center" border="0" cellspacing="0" cellpadding="0" style="text-align:center;">
                                                            <tr>
                                                                <td class="text-button" style="background:#fecc7b; color:#000000; font-family:'Playfair Display', Georgia,serif; font-size:14px; line-height:18px; padding:12px 30px; text-align:center; border-radius:25px; text-transform:uppercase;"><a href="mailto:bps5104@bps.go.id?subject= Help" target="_blank" class="link" style="color:#000001; text-decoration:none;"><span class="link" style="color:#000001; text-decoration:none;">CLICK HERE</span></a></td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <!-- END Button -->

												<tr>
                                                    <td class="text-center pb30" style="color:#666666; font-family:'Muli', Arial,sans-serif; font-size:12px; line-height:30px; text-align:center; padding-bottom:30px;">
														<hr style =" margin: 25px auto; width: 50%;  height: 2px;  background-color: #f90;  border: none;" />
														Jika ingin berhenti berlangganan berita dari BPS Kabupaten Gianyar, silahkan unsubscribe dengan cara: <b> <A HREF="mailto:bps5104@bps.go.id?subject= Unsubscribe">Klik link unsubscribe ini</A> </b>  atau kirim email ke bps5104@bps.go.id dengan subject Unsubscribe.
													</td>
                                                </tr>

                                            </table>

                                        </td>
                                    </tr>

                                </table>
                                <!-- END CTA -->


                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    
    
    
    """


    #pdfkit.from_string(html, 'out.pdf')


    msg.attach(MIMEText(html , 'html'))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(newsletterAdress, newsletterPassword)
    mailserver.sendmail(newsletterAdress, recipientAdress, msg.as_string())
    mailserver.quit()
    print(" EMAIL SEND !!")