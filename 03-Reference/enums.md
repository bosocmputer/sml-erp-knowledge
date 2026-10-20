---
tags: [sml, reference, enums, generated]
---
# Enum (รหัสตัวเลข → ความหมาย)

> สร้างอัตโนมัติด้วย `scripts/gen_enums.py` จากโค้ด — ค่าเป็นลำดับเริ่ม 0 ถ้าไม่ได้กำหนด `= n` (กติกา C#)
> ใช้ตีความคอลัมน์ตัวเลขใน DB เช่น ประเภทภาษี/สถานะ — ยืนยันกับโค้ดที่เขียนคอลัมน์นั้นก่อนสรุป

trans_type ใน ic_trans / ic_trans_detail (จาก SMLDocs): 1 = เจ้าหนี้, 2 = ลูกหนี้, 3 = สินค้า · trans_flag ดู [[trans_flag]] · กลับไป [[00-Index]]

## AccountTypeEnum

`SMLERPGlobal/_docFormatClass.cs`

0=Debit, 1=Credit, 2=Both

## _productCostType

`SMLERPGlobal/_global.cs`

0=ปรกติ, 1=รวมต้นทุนแฝง, 2=เคลื่อนไหวสินค้า

## _androidDisplayEnum

`SMLERPGlobal/_global.cs`

0=Clear, 1=ItemName, 2=Unit, 3=Qty, 4=Price, 5=Total, 6=Amount, 7=AmountWord

## _priceGridType

`SMLERPGlobal/_global.cs`

0=ราคาปรกติ, 1=ราคาตามกลุ่มลูกค้า, 2=ราคาตามลูกค้า, 3=ราคาตามเจ้าหนี้, 4=ลดทั่วไป, 5=ลดตามกลุ่มลูกค้า, 6=ลดตามลูกค้า

## _priceListType

`SMLERPGlobal/_global.cs`

0=ว่าง, 1=ซื้อ_ราคาซื้อทั่วไป, 2=ซื้อ_ราคาซื้อตามเจ้าหนี้, 3=ขาย_ราคาขายทั่วไป, 4=ขาย_ราคาขายตามกลุ่มลูกค้า, 5=ขาย_ราคาขายตามลูกค้า, 6=ขาย_ราคาขายมาตรฐาน

## _vatTypeEnum

`SMLERPGlobal/_global.cs`

0=ภาษีแยกนอก, 1=ภาษีรวมใน, 2=ยกเว้นภาษี, 3=ไม่กระทบภาษี, -1=ว่าง

## _autoRunType

`SMLERPGlobal/_global.cs`

0=ใบกำกับภาษี, 1=บัญชี_ข้อมูลรายวัน, 2=ข้อมูลรายวัน, 3=สินค้า, 4=ลูกหนี้, 5=เจ้าหนี้, 6=เจ้าหนี้_ลูกหนี้รายวัน, 7=เงินเดือน_พนักงาน, 8=เงินเดือน_ขาด, 9=เงินเดือน_ลา, 10=เงินเดือน_มาสาย, 11=เงินเดือน_ค่าล่วงเวลา, 12=เงินเดือน_อัตราภาษีเงินได้, 13=เงินเดือน_รายละเอียดการทำงาน, 14=เงินเดือน_คำนวนเงินเดือน, 15=เงินเดือน_จ่ายภาษีรายเดือน, 16=เงินเดือน_คำนวนภาษี, 17=POS_รับเงินทอน, 18=POS_ส่งเงิน, 19=ใบสั่งอาหาร, 20=ว่าง

## _screenPayrollEnum

`SMLERPGlobal/_global.cs`

0=คำนวนเงินเดือน, 1=คำนวนภาษีรายเดือน, 2=คำนวนภาษีรายปี, 3=ภงด_1, 4=ภงด_1_ใบแนบ, 5=สปส_1_10_ส่วนที่1, 6=สปส_1_10_ส่วนที่2, 7=สลิปเงินเดือน, 8=ภงด_1_ก, 9=ภงด_1_ก_ใบแนบ, 10=ภงด_91, 11=รายละเอียดพนักงาน_ลูกจ้าง_ตามประเภท, 12=รายละเอียดพนักงาน_ลูกจ้าง_ตามเงินเดือน, 13=รายละเอียดการขาดงาน, 14=รายละเอียดการลางาน, 15=รายละเอียดการมาสาย, 16=รายละเอียดการทำงานล่วงเวลา, 17=รายละเอียดเงินเดือน_ค่าจ้าง_ตามประเภทลูกจ้าง, 18=รายละเอียดเงินได้_เงินหัก_ประจำเดือน, 19=รายงานภาษีเงินได้_รายเดือน, 20=รายงานภาษีเงินได้_รายปี, 21=รายงานสรุป_การทำงาน_พนักงาน_ลูกจ้าง, 22=รายงานสรุป_การจ่ายเงินเดือน_ค้าจ้าง_ทั้งหมด, 23=รายงานเปรียบเทียบ_การจ่ายเงินเดือน_ค้าจ้าง, 24=รายละเอียดเงินเดือน_ค่าจ้างทั้งปี

## _depositAdvanceEnum

`SMLERPGlobal/_global.cs`

0=รับเงินล่วงหน้า, 1=รับเงินมัดจำ, 2=จ่ายเงินล่วงหน้า, 3=จ่ายเงินมัดจำ

## ProjectAllowcateEnum

`SMLERPGlobal/_global.cs`

0=แผนก, 1=โครงการ, 2=การจัดสรร, 3=หน่วยงาน, 4=งาน

## _chqTypeEnum

`SMLERPGlobal/_global.cs`

0=ว่าง, 1=เช็ครับ, 2=เช็คจ่าย, 3=บัตรเครดิต, 4=wallet

## _chequeReceiveStatusEnum

`SMLERPGlobal/_global.cs`

0=เช็ครับในมือ, 1=เช็ครับนำฝาก, 2=เช็ครับผ่าน, 3=เช็ครับคืน, 21=wallet

## _transTypeEnum

`SMLERPGlobal/_global.cs`

0=ว่าง, 1=สินค้า, 2=ขาย_ลูกหนี้, 3=ซื้อ_เจ้าหนี้, 4=เจ้าหนี้, 5=ลูกหนี้

## _transSystemEnum

`SMLERPGlobal/_global.cs`

0=ว่าง, 1=สินค้า, 2=ซื้อ, 3=ขาย, 4=เจ้าหนี้, 5=ลูกหนี้, 6=เงินสดธนาคาร, 7=บัญชี

## OEMVersion

`MyLib/OEMVersion.cs`

0=None, 1=IMEX

## eWalletNameEnum

`MyLib/PaymentGateway/PaymentQRDetail.cs`

0=None, 1=BCEL, 2=LUGENT_THAIQR, 3=LUGENT_ALIPAY, 4=LUGENT_WECHAT, 5=LUGENT_LINEPAY, 6=LUGENT_WAVES, 7=THAI_PROMPTPAY, 8=THAI_QR_PROMPTPAY, 9=THAI_QR_WALLET, 10=KBANK_PROMPTPAY, 11=KBANK_QR_CREDIT

## FillType

`MyLib/RoundedGroupBox.cs`

0=Fill, 1=LinearGradient

## LineStyle

`MyLib/RoundedGroupBox.cs`

0=Solid, 1=Dashed

## OpenMode

`MyLib/_cashDrawer.cs`

0=ComPort, 1=Printer

## State

`MyLib/_fancyButton.cs`

0=None, 1=Hover, 2=Pressed

## Style

`MyLib/_fancyButton.cs`

0=Default, 1=Flat

## _databaseType

`MyLib/_global.cs`

0=PostgreSql, 1=MySql, 2=MicrosoftSQL2000, 3=MicrosoftSQL2005, 4=Oracle, 5=Firebird

## _versionType

`MyLib/_global.cs`

0=Null, 1=SMLPOS, 2=SMLPOSLite, 3=SMLPOSStarter, 4=SMLAccountProfessional, 5=SMLAccountPOSProfessional, 6=SMLGL, 7=SMLHP, 8=SMLPP, 9=SMLAccount, 10=SMLColorStore, 11=SMLThai7, 12=SMLPayroll, 13=SMLServiceCenter, 14=SMLHealthy, 15=SMLPOSMED, 16=SMLTomYumGoong, 17=SMLTomYumGoongPro, 18=ICCManage, 19=SMLPickAndPack, 20=SMLIMS, 21=IMSPOS, 22=IMSAccountPro, 23=SMLActiveSync, 24=SMLAccountPOS, 25=SMLBIllFree, 26=SMLGeneralLedger, 27=SMLCM, 28=SMLMerchant, 29=SMLPOSCoffee

## _languageEnum

`MyLib/_global.cs`

0=English, 1=Thai, 2=Malayu, 3=Chainese, 4=India, 5=Lao, 6=Null, 7=Khmer

## GroupBoxGradientMode

`MyLib/_grouper.cs`

4=None, 3=BackwardDiagonal, 2=ForwardDiagonal, 0=Horizontal, 1=Vertical

## LVS_EX

`MyLib/_listViewXP.cs`

0=LVS_EX_GRIDLINES, 1=LVS_EX_SUBITEMIMAGES, 2=LVS_EX_CHECKBOXES, 3=LVS_EX_TRACKSELECT, 4=LVS_EX_HEADERDRAGDROP, 5=LVS_EX_FULLROWSELECT, 6=LVS_EX_ONECLICKACTIVATE, 7=LVS_EX_TWOCLICKACTIVATE, 8=LVS_EX_FLATSB, 9=LVS_EX_REGIONAL, 10=LVS_EX_INFOTIP, 11=LVS_EX_UNDERLINEHOT, 12=LVS_EX_UNDERLINECOLD, 13=LVS_EX_MULTIWORKAREAS, 14=LVS_EX_LABELTIP, 15=LVS_EX_BORDERSELECT, 16=LVS_EX_DOUBLEBUFFER, 17=LVS_EX_HIDELABELS, 18=LVS_EX_SINGLEROW, 19=LVS_EX_SNAPTOGRID, 20=LVS_EX_SIMPLESELECT

## LVM

`MyLib/_listViewXP.cs`

0=LVM_FIRST, 1=LVM_SETEXTENDEDLISTVIEWSTYLE, 2=LVM_GETEXTENDEDLISTVIEWSTYLE

## Parameters

`MyLib/_mathParser.cs`

0=A, 1=B, 2=C, 3=D, 4=E, 5=F, 6=G, 7=H, 8=I, 9=J, 10=K, 11=L, 12=M, 13=N, 14=O, 15=P, 16=Q, 17=R, 18=S, 19=T, 20=U, 21=V, 22=W, 23=X, 24=Y, 25=Z

## _databaseColumnType

`MyLib/_myDatabaseFrameWork.cs`

0=String, 1=Datetime, 2=Number, 3=Image

## State

`MyLib/_myImageButton.cs`

0=None, 1=Hover, 2=Pressed

## Style

`MyLib/_myImageButton.cs`

0=Default, 1=Flat

## ListViewGroupMask

`MyLib/_myListView.cs`

0=None, 1=Header, 2=Footer, 3=State, 4=Align, 5=GroupId, 6=SubTitle, 7=Task, 8=DescriptionTop, 9=DescriptionBottom, 10=TitleImage, 11=ExtendedImage, 12=Items, 13=Subset, 14=SubsetItems

## ListViewGroupState

`MyLib/_myListView.cs`

0=Normal, 1=Collapsed, 2=Hidden, 4=NoHeader, 8=Collapsible, 16=Focused, 32=Selected, 64=SubSeted, 128=SubSetLinkFocused

## MemoryBoxResult

`MyLib/_myMessageBox.cs`

0=Yes, 1=YesToAll, 2=No, 3=NoToAll, 4=Cancel

## MemoryBoxButton

`MyLib/_myMessageBox.cs`

0=YesToAllNoToAll, 1=CustomOK, 2=TwoButton, 3=ThreeButton

## State

`MyLib/_myPanelVista.cs`

0=None, 1=Hover, 2=Pressed

## Style

`MyLib/_myPanelVista.cs`

0=Default, 1=Flat

## GradientMode

`MyLib/_myProgressBar.cs`

0=Vertical, 1=VerticalCenter, 2=Horizontal, 3=HorizontalCenter, 4=Diagonal

## DragCursorType

`MyLib/_myTreeViewDragDrop.cs`

0=None, 1=DragIcon, 2=Custom

## HttpVerb

`MyLib/_restClient.cs`

0=GET, 1=POST, 2=PUT, 3=DELETE

## CLSCTX

`SMLERPControl/DShowNET/DsBugWO.cs`

0=Inproc, 1=Server, 2=All

## DsEvCode

`SMLERPControl/DShowNET/DsControl.cs`

0=None, 1=Complete, 2=UserAbort, 3=ErrorAbort, 4=Time, 5=Repaint, 6=StErrStopped, 7=StErrStPlaying, 8=ErrorStPlaying, 9=PaletteChanged, 10=VideoSizeChanged, 11=QualityChange, 12=ShuttingDown, 13=ClockChanged, 14=Paused, 15=OpeningFile, 16=BufferingData, 17=FullScreenLost, 18=Activate, 19=NeedRestart, 20=WindowDestroyed, 21=DisplayChanged, 22=Starvation, 23=OleEvent, 24=NotifyWindow, 25=DvdDomChange, 26=DvdTitleChange, 27=DvdChaptStart, 28=DvdAudioStChange, 29=DvdSubPicStChange, 30=DvdAngleChange, 31=DvdButtonChange, 32=DvdValidUopsChange, 33=DvdStillOn, 34=DvdStillOff, 35=DvdCurrentTime, 36=DvdError, 37=DvdWarning, 38=DvdChaptAutoStop, 39=DvdNoFpPgc, 40=DvdPlaybRateChange, 41=DvdParentalLChange, 42=DvdPlaybStopped, 43=DvdAnglesAvail, 44=DvdPeriodAStop, 45=DvdButtonAActivated, 46=DvdCmdStart, 47=DvdCmdEnd, 48=DvdDiscEjected, 49=DvdDiscInserted, 50=DvdCurrentHmsfTime, 51=DvdKaraokeMode

## PinDirection

`SMLERPControl/DShowNET/DsCore.cs`

0=Input, 1=Output

## SeekingCapabilities

`SMLERPControl/DShowNET/DsCore.cs`

0=CanSeekAbsolute, 1=CanSeekForwards, 2=CanSeekBackwards, 3=CanGetCurrentPos, 4=CanGetStopPos, 5=CanGetDuration, 6=CanPlayBackwards, 7=CanDoSegments, 8=Source

## SeekingFlags

`SMLERPControl/DShowNET/DsCore.cs`

0=NoPositioning, 1=AbsolutePositioning, 2=RelativePositioning, 3=IncrementalPositioning, 4=PositioningBitsMask, 5=SeekToKeyFrame, 6=ReturnTime, 7=Segment, 8=NoFlush

## DvdGraphFlags

`SMLERPControl/DShowNET/DsDVD.cs`

0=Default, 1=HwDecPrefer, 2=HwDecOnly, 3=SwDecPrefer, 4=SwDecOnly, 5=NoVpe

## DvdStreamFlags

`SMLERPControl/DShowNET/DsDVD.cs`

0=None, 1=Video, 2=Audio, 3=SubPic

## DvdCmdFlags

`SMLERPControl/DShowNET/DsDVD.cs`

0=None, 1=Flush, 2=SendEvt, 3=Block, 4=StartWRendered, 5=EndARendered

## DvdMenuID

`SMLERPControl/DShowNET/DsDVD.cs`

2=Title, 3=Root, 4=Subpicture, 5=Audio, 6=Angle, 7=Chapter

## DvdRelButton

`SMLERPControl/DShowNET/DsDVD.cs`

1=Upper, 2=Lower, 3=Left, 4=Right

## DvdOptionFlag

`SMLERPControl/DShowNET/DsDVD.cs`

1=ResetOnStop, 2=NotifyParentalLevelChange, 3=HmsfTimeCodeEvt

## DvdAudioLangExt

`SMLERPControl/DShowNET/DsDVD.cs`

0=NotSpecified, 1=Captions, 2=VisuallyImpaired, 3=DirectorComments1, 4=DirectorComments2

## DvdSubPicLangExt

`SMLERPControl/DShowNET/DsDVD.cs`

0=NotSpecified, 1=CaptionNormal, 2=CaptionBig, 3=CaptionChildren, 5=ClosedNormal, 6=ClosedBig, 7=ClosedChildren, 9=Forced, 13=DirectorCmtNormal, 14=DirectorCmtBig, 15=DirectorCmtChildren

## DvdDomain

`SMLERPControl/DShowNET/DsDVD.cs`

1=FirstPlay, 2=VideoManagerMenu, 3=VideoTitleSetMenu, 4=Title, 5=Stop

## DvdVideoCompress

`SMLERPControl/DShowNET/DsDVD.cs`

0=Other, 1=Mpeg1, 2=Mpeg2

## DvdAudioAppMode

`SMLERPControl/DShowNET/DsDVD.cs`

0=None, 1=Karaoke, 2=Surround, 3=Other

## DvdAudioFormat

`SMLERPControl/DShowNET/DsDVD.cs`

0=Ac3, 1=Mpeg1, 2=Mpeg1Drc, 3=Mpeg2, 4=Mpeg2Drc, 5=Lpcm, 6=Dts, 7=Sdds, 8=Other

## DvdSubPicType

`SMLERPControl/DShowNET/DsDVD.cs`

0=NotSpecified, 1=Language, 2=Other

## DvdSubPicCoding

`SMLERPControl/DShowNET/DsDVD.cs`

0=RunLength, 1=Extended, 2=Other

## DvdTitleAppMode

`SMLERPControl/DShowNET/DsDVD.cs`

0=NotSpecified, 1=Karaoke, 3=Other

## DvdDiscSide

`SMLERPControl/DShowNET/DsDVD.cs`

1=A, 2=B

## DvdCharSet

`SMLERPControl/DShowNET/DsDVD.cs`

0=Unicode, 1=Iso646, 2=Jis, 3=Iso8859, 4=SiftJis

## DvdAudioCaps

`SMLERPControl/DShowNET/DsDVD.cs`

0=Ac3, 1=Mpeg2, 2=Lpcm, 3=Dts, 4=Sdds

## AMTunerSubChannel

`SMLERPControl/DShowNET/DsExtend.cs`

-2=NoTune, -1=Default

## AMTunerSignalStrength

`SMLERPControl/DShowNET/DsExtend.cs`

-1=NA, 0=NoSignal, 1=SignalPresent

## AMTunerModeType

`SMLERPControl/DShowNET/DsExtend.cs`

0=Default, 1=TV, 2=FMRadio, 3=AMRadio, 4=Dss

## AMTunerEventType

`SMLERPControl/DShowNET/DsExtend.cs`

0=Changed

## AnalogVideoStandard

`SMLERPControl/DShowNET/DsExtend.cs`

0=None, 1=NTSC_M, 2=NTSC_M_J, 3=NTSC_433, 4=PAL_B, 5=PAL_D, 6=PAL_G, 7=PAL_H, 8=PAL_I, 9=PAL_M, 10=PAL_N, 11=PAL_60, 12=SECAM_B, 13=SECAM_D, 14=SECAM_G, 15=SECAM_H, 16=SECAM_K, 17=SECAM_K1, 18=SECAM_L, 19=SECAM_L1, 20=PAL_N_COMBO

## TunerInputType

`SMLERPControl/DShowNET/DsExtend.cs`

0=Cable, 1=Antenna

## PlayState

`SMLERPControl/_WebCam.cs`

0=Init, 1=Stopped, 2=Paused, 3=Running

## _TransTypeEnum

`SMLERPControl/_bank/_bankControl.cs`

0=Cash, 1=Checks, 2=PettyCash, 3=CreditCard

## _bankControlTypeEnum

`SMLERPControl/_bank/_bankControl.cs`

0=ฝากเงิน, 1=cash_payin_cancle, 2=cash_withdraw, 3=cash_withdraw_cancle, 4=received, 5=received_cancle, 6=payment, 7=payment_cancle, 8=interest_received, 9=interest_received_cancle, 10=interest_payment, 11=interest_payment_cancle, 12=cash_transfer_received, 13=cash_transfer_received_cancle, 14=cash_transfer_payment, 15=cash_transfer_payment_cancle, 16=in_payin, 17=in_payin_cancle, 18=in_return, 19=in_return_cancle, 20=in_honor, 21=in_honor_cancle, 22=in_change, 23=in_change_cancle, 24=in_new, 25=in_new_cancle, 26=out_return, 27=out_return_cancle, 28=out_honor, 29=out_honor_cancle, 30=out_change, 31=out_change_cancle, 32=credit_money, 33=credit_cancel, 34=petty_receive, 35=petty_receive_cancle, 36=petty_request, 37=petty_request_cancle, 38=petty_return, 39=petty_return_cancle, 40=เช็ครับ, 41=out_payment, 42=in_discount, 43=in_cancel, 44=out_cancel, 45=petty_payment, 46=petty_request_approve, 47=petty_request_approve_cancel, 48=petty_clear

## _chqListControlTypeEnum

`SMLERPControl/_bank/_chqListControl.cs`

0=ว่าง, 1=ทะเบียนเช็ครับ, 2=ทะเบียนเช็คจ่าย, 3=ทะเบียนบัตรเครดิต

## _creditMasterControlTypeEnum

`SMLERPControl/_bank/_creditMasterControl.cs`

0=credit_master_receive, 1=credit_master_payment

## _pettyCashMasterControlTypeEnum

`SMLERPControl/_bank/_pettyCashMasterControl.cs`

0=ว่าง, 1=pettycash_master

## CouponValidateErrorEnum

`SMLERPControl/_coupon/_couponValidator.cs`

0=NONE, 1=COUPON_NOT_FOUND, 2=COUPON_CUSTOMERCODE_MIS_MATCH, 3=COUPON_USE_BEFORE_DATE_START, 4=COUPON_EXPIRE, 5=COUPON_CANCEL, 6=COUPON_ALREADY_USED, 7=COUPON_BRANCH_MIS_MATCH, 8=COUPON_CUSTOMER_GROUP_MIS_MATCH, 9=COUPON_DAY_USE_MIS_MATCH, 10=COUPON_PRODUCT_ATTRIBUTE_MIS_MATCH, 11=COUPON_PRODUCT_MIS_MATCH, 12=COUPON_CUSTOMER_TYPE_MIS_MATCH, 13=COUPON_SALE_AMOUNT_MIS_MATCH

## _controlTypeEnumGrid

`SMLERPControl/_customer/_screen_ar_grid.cs`

0=ArContactorGrid, 1=ApContactorGrid, 2=ArItemGrid, 3=M_congenital_disease, 4=M_allergic

## _controlTypeEnum

`SMLERPControl/_customer/_screen_ar_main.cs`

0=Ar, 1=ArDetail, 2=ArDetailBill, 3=ArDetailCredit, 4=ArDetailGroup, 5=ArDetailDimension, 6=ArDealer, 7=ArDealerHealthy, 8=ArDetailHealthy, 9=ArTaxOnly

## _arrowObjectStyle

`SMLERPControl/_flow/_arrowObject.cs`

0=LeftToRightCenter, 1=RightToLeftCenter, 2=TopToDownCenter, 3=DownToTopCenter

## TableDisplayPOSOName

`SMLERPControl/_gridProperty.cs`

0=POBilling, 1=POInvestigate, 2=POQuotation, 3=POSOCreditnote, 4=POGoodreceive, 5=PORequest, 6=POPrice, 7=POInquiry

## TableDisplayICName

`SMLERPControl/_gridProperty.cs`

0=StockBalance, 1=StockRequest, 2=StockReturn, 3=StockChecking, 4=StockAdjust, 5=StockTransfer, 6=ItemBuild, 7=InventoryBarcode, 8=InventoryReplace, 9=InventoryAppend, 10=InventorySet, 11=InventoryWarehouse, 12=InventoryFinishGood, 13=InventoryCustomer, 14=InventorySupplier

## SearchItemFormat

`SMLERPControl/_gridProperty.cs`

0=Normal, 1=Advance

## SearchMasFormat

`SMLERPControl/_gridProperty.cs`

0=Style1, 1=Style2

## _stockBalanceType

`SMLERPControl/_icInfoProcess.cs`

0=ยอดคงเหลือตามสินค้า, 1=ยอดคงเหลือตามคลัง, 2=ยอดคงเหลือตามที่เก็บ, 3=ยอดคงเหลือตามLOT, 4=ยอดคงเหลือตามLOT_ที่เก็บ, 5=ยอดคงเหลือตามLOT_ที่เก็บ_เรียงตามเอกสาร_IMEX

## VisibleType

`SMLERPControl/_sideBar/OutlookStyleSidebar.cs`

1=Visible, 2=Unvisible

## MoveType

`SMLERPControl/_sideBar/OutlookStyleSidebar.cs`

0=Up, 1=Down

## _controlTypeEnum

`SMLERPControl/supplier/_screen_ap_main.cs`

0=Ap, 1=ApDetail, 2=ApDetailBill, 3=ApDetailCredit, 4=ApDetailGroup, 5=ApDetailDimension

## _formEnum

`SMLInventoryControl/_global.cs`

0=ใบเสนอราคา, 1=ขาย_ขายสินค้าและบริการ, 2=ขาย_ขายสินค้าและบริการ_ici, 3=ขาย_ใบสั่งขาย, 4=ขาย_สั่งจองสินค้าและสั่งซื้อสินค้า, 5=ขาย_เพิ่มหนี้, 6=ขาย_รับเงินล่วงหน้า, 7=ขาย_คืนเงินล่วงหน้า, 8=ขาย_ลดหนี้, 9=ใบกำกับภาษี, 10=ใบแจ้งหนี้, 11=ใบซื้อสินค้าและบริการ, 12=ซื้อ_ซื้อสินค้าและค่าบริการ, 13=ซื้อ_ใบสั่งซื้อ, 14=ซื้อ_ซื้อสินค้าเพิ่มหนี้หรือราคาผิด, 15=ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด, 16=ซื้อ_จ่ายเงินมัดจำหรือเงินล่วงหน้า, 17=ซื้อ_คืนเงินมัดจำหรือเงินล่วงหน้า, 18=เจ้าหนี้_ใบรับวางบิล, 19=เจ้าหนี้_ใบจ่ายชำระหนี้, 20=ลูกหนี้_ใบวางบิล, 21=ลูกหนี้_รับชำระหนี้, 22=สินค้า_รับสินค้าสำเร็จรูป, 23=สินค้า_เบิกสินค้าวัตถุดิบ, 24=สินค้า_รับคืนสินค้าจากการเบิก, 25=สินค้า_โอนเข้า, 26=สินค้า_โอนออก, 27=ซื้อ_พาเชียล_ตั้งหนี้, 28=ซื้อ_พาเชียล_รับสินค้า, 29=ซื้อ_พาเชียล_ราคาผิด, 30=ซื้อ_พาเชียล_ลดหนี้, 31=ซื้อ_พาเชียล_เพิ่มหนี้

## _transHistoryType

`SMLInventoryControl/_transHistory.cs`

0=ประวัติการขาย, 1=ประวัติการซื้อ

## State

`SMLPOSControl/_designer/_object/_button.cs`

0=None, 1=Hover, 2=Pressed

## Style

`SMLPOSControl/_designer/_object/_button.cs`

0=Default, 1=Flat

## _posItemsFieldEnum

`SMLPOSControl/_designer/_object/_posItemsTable.cs`

0=ItemCode, 1=ItemName, 2=Qty, 3=UnitPrice, 4=Total

## _tableColumnType

`SMLPOSControl/_designer/_object/_posItemsTable.cs`

0=String, 1=Number, 2=Date

## printcopyGridType

`SMLPOSControl/_food/_kitchenControl.cs`

0=Order, 1=Cancel

## _posControls

`SMLPOSControl/_global.cs`

0=Panel, 1=Button, 2=Label, 3=ItemsTable, 4=ItemButtonPanel, 5=Image, 6=HTML, 7=TextBox, 8=SearchLevel

## _printSlipTextStyle

`SMLPOSControl/_global.cs`

0=Left, 1=Right, 2=Center

## _reportTypeEnum

`SMLERPReportTool/_global.cs`

0=ว่าง, 1=สินค้า, 2=ขาย_ลูกหนี้, 3=ซื้อ_เจ้าหนี้, 4=เจ้าหนี้, 5=ลูกหนี้, 6=เช็ค, 7=บัตรเครดิต, 8=เงินสดธนาคาร, 9=สินค้า_Serial, 10=ธนาคาร

## _reportVatNumberType

`SMLERPReportTool/_global.cs`

0=ปรกติ, 1=แสดงตัวเลขแบบรวมในทั้งหมด, 2=แสดงตัวเลขแบบแยกนอกทั้งหมด

## _reportEnum

`SMLERPReportTool/_global.cs`

0=ขาย_, 1=ขาย_รับเงินล่วงหน้า, 2=ขาย_รับเงินล่วงหน้า_ยกเลิก, 3=ขาย_รับเงินล่วงหน้า_คืน, 4=ขาย_รับเงินล่วงหน้า_คืน_ยกเลิก, 5=ขาย_รับเงินล่วงหน้า_รายงานยอดคงเหลือ, 6=ขาย_รับเงินล่วงหน้า_รายงานตัดเงิน, 7=ขาย_รับเงินมัดจำ, 8=ขาย_รับเงินมัดจำ_ยกเลิก, 9=ขาย_รับเงินมัดจำ_คืน, 10=ขาย_รับเงินมัดจำ_คืน_ยกเลิก, 11=ขาย_รับเงินมัดจำ_รายงานยอดคงเหลือ, 12=ขาย_รับเงินมัดจำ_รายงานตัดเงิน, 13=ขาย_สั่งขาย, 14=ขาย_สั่งขาย_ยกเลิก, 15=ขาย_สั่งขาย_อนุมัติ, 16=ขาย_สั่งขาย_สถานะ, 17=ขาย_ขายสินค้าและบริการ, 18=ขาย_ขายสินค้าและบริการ_ลดหนี้_เพิ่มหนี้, 19=ขาย_ขายสินค้าและบริการ_รายงานการออกใบกำกับภาษีอย่างเต็ม, 20=ขาย_ขายสินค้าและบริการ_ยกเลิก, 21=ขาย_เพิ่มหนี้สินค้าราคาผิด, 22=ขาย_เพิ่มหนี้สินค้าราคาผิด_ยกเลิก, 23=ขาย_รับคืนสินค้า, 24=ขาย_รับคืนสินค้า_ยกเลิก, 25=ขาย_สั่งจองและสั่งซื้อสินค้า, 26=ขาย_สั่งจองและสั่งซื้อสินค้า_ยกเลิก, 27=ขาย_สั่งจองและสั่งซื้อสินค้า_อนุมัติ, 28=ขาย_สั่งจองและสั่งซื้อสินค้า_สถานะ, 29=ขาย_รายงานใบเสนอซื้อสินค้า, 30=ขาย_รายงานลดหนี้สินค้าราคาผิด, 31=ขาย_เสนอราคา, 32=ขาย_เสนอราคา_ยกเลิก, 33=ขาย_เสนอราคา_อนุมัติ, 34=ขาย_เสนอราคา_สถานะ, 35=ขาย_รายงานขายสินค้าแยกตามสินค้า, 36=ซื้อ_ซื้อสินค้าและบริการ, 37=ซื้อ_ซื้อสินค้าและบริการ_ยกเลิก, 38=ซื้อ_จ่ายเงินล่วงหน้า, 39=ซื้อ_จ่ายเงินล่วงหน้า_ยกเลิก, 40=ซื้อ_จ่ายเงินล่วงหน้า_รับคืน, 41=ซื้อ_จ่ายเงินล่วงหน้า_รับคืน_ยกเลิก, 42=ซื้อ_จ่ายเงินมัดจำ, 43=ซื้อ_จ่ายเงินมัดจำ_ยกเลิก, 44=ซื้อ_จ่ายเงินมัดจำ_รับคืน, 45=ซื้อ_จ่ายเงินมัดจำ_รับคืน_ยกเลิก, 46=ซื้อ_รายงานยอดคงเหลือเงินจ่ายล่วงหน้า, 47=ซื้อ_รายงานตัดเงินจ่ายล่วงหน้า, 48=ซื้อ_รายงานยอดคงเหลือเงินมัดจำจ่าย, 49=ซื้อ_รายงานตัดเงินมัดจำจ่าย, 50=ซื้อ_รายงานซื้อสินค้าแยกตามสินค้า, 51=ซื้อ_รายงานใบสั่งซื้อ, 52=ซื้อ_รายงานอนุมัติใบสั่งซื้อ, 53=ซื้อ_รายงานยกเลิกใบสั่งซื้อ, 54=ซื้อ_รายงานสถานะใบสั่งซื้อ, 55=ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด, 56=ซื้อ_ส่งคืนสินค้าลดหนี้ราคาผิด_ยกเลิก, 57=ซื้อ_เพิ่มหนี้ราคาผิด, 58=ซื้อ_เพิ่มหนี้ราคาผิด_ยกเลิก, 59=ซื้อ_ใบเสนอซื้อ, 60=ซื้อ_ใบเสนอซื้อ_อนุมัติ, 61=ซื้อ_ใบเสนอซื้อ_ยกเลิก, 62=ซื้อ_ใบเสนอซื้อ_สถานะ, 63=ซื้อ_พาเชียล_รับสินค้า, 64=ซื้อ_พาเชียล_ส่งคืนสินค้าหรือราคาผิด, 65=ซื้อ_พาเชียล_ตั้งหนี้, 66=ซื้อ_พาเชียล_เพิ่มหนี้, 67=ซื้อ_พาเชียล_ลดหนี้, 68=ซื้อ_รายงานค้างรับตามใบสั่งซื้อ, 69=สินค้า_รายงานรายละเอียดสินค้า, 70=สินค้า_รายงานรายละเอียดบาร์โค๊ด, 71=สินค้า_รายงานสูตรสีผสม, 72=สินค้า_รายงานราคาขายสินค้า, 73=สินค้า_รายงานราคาซื้อสินค้า, 74=สินค้า_รายงานสินค้าที่ไม่มีการเคลื่อนไหว, 75=สินค้า_รายงานสรุปเคลื่อนไหวตามปริมาณ, 76=สินค้า_รายงานเคลื่อนไหว, 77=สินค้า_รายงานโอนสินค้าและวัตถุดิบ, 78=สินค้า_รายงานโอนสินค้าและวัตถุดิบ_ยกเลิก, 79=สินค้า_รายงานบัญชีคุมพิเศษ …

## DepreciationMode

`SMLProcess/_asProcess.cs`

0=จำนวนวันจริง, 1=จำนวนวันบัญชี, 2=จำนวนวันสรรพากร

## DepreciationBy

`SMLProcess/_asProcess.cs`

0=ปี, 1=เดือน, 2=วัน

## _sendProcessType

`SMLProcess/_sendProcess.cs`

0=ap_supplier

