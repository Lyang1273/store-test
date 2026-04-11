import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import RinUI
import "../components"

FluentPage {
    title: qsTr("主页")

    Column {
        Layout.fillWidth: true
        spacing: 3

        Text {
            typography: Typography.BodyStrong
            text: qsTr("类型1")
        }
        InfoClip {
            iconSource: "./assets/icon.png"
            title: "RinUI"
            desc: "A Fluent Design System implementation for Qt Quick"
            url: "https://mobile.yangkeduo.com/arbiter_checkered_indite.html?F673716A21=TxXlj7TTpB2xu&modulate_artless_bridle=X2QpduIKvkt9jOUYVRLWzg%2C%2C&campaign=cutprice&sub_campaign=mtpgifts&_pdd_fs=1&_ex_sid=mtpgifts_scan1&share_group_sn=AXFOQ5DZYJJLKJUHMRODU2PWIM_GEXDA40AFE38319E93222&pearl_share_uin=AXFOQ5DZYJJLKJUHMRODU2PWIM_GEXDA&trace_id=exr-9rf-0g6&__wls_rt=1&__wls_lt=1&__wls_fm=n"
        }
        
        //GridLayout {
        //    columns: 3
        //    spacing: 10
        //    layoutDirection: Qt.LeftToRight
        //    Repeater {
        //        model: 6
        //        Text {
        //            text: modelData
        //        }
        //    }
        //}
        Text {
            typography: Typography.BodyStrong
            text: qsTr("类型2")
        }
        //GridLayout {
        //    columns: 3
        //    spacing: 10
        //    layoutDirection: Qt.LeftToRight
        //    Repeater {
        //        model: 6
        //        Text {
        //            text: modelData
        //        }
        //    }
        //}
        Text {
            typography: Typography.BodyStrong
            text: qsTr("类型3")
        }
        //GridLayout {
        //    columns: 3
        //    spacing: 10
        //    layoutDirection: Qt.LeftToRight
        //    Repeater {
        //        model: 6
        //        Text {
        //            text: modelData
        //        }
        //    }
        //}
    }
}