import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import RinUI

Clip {
    id: root
    width: 360
    height: 88
    radius: 12

    property string url: modelData?.url ?? ""
    property string iconSource: modelData?.icon ?? null
    property string title: modelData?.title ?? ""
    property string desc: modelData?.desc ?? ""
    property bool isNew: modelData?.added ?? false
    property bool isUpdated: modelData?.updated ?? false

    InfoBadge {
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.margins: 12
        width: 8
        height: 8
        text: "·"
        visible: root.isNew || root.isUpdated
    }

    RowLayout {
        anchors.fill: parent
        anchors.leftMargin: 22
        anchors.rightMargin: 22
        spacing: 16

        Image {
            Layout.alignment: Qt.AlignVCenter
            source: root.iconSource
            fillMode: Image.PreserveAspectFit
            Layout.preferredWidth: 40
            Layout.preferredHeight: 40
        }
        Column {
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignVCenter
            Text {
                width: parent.width
                typography: Typography.BodyStrong
                font.pixelSize: 13
                text: root.title
            }
            Text {
                width: parent.width
                typography: Typography.Caption
                color: Theme.currentTheme.colors.textSecondaryColor
                text: root.desc
            }
        }
        Button {
            text: qsTr("Open")
            onClicked: {
                if (root.url) {
                    backend.downloadFile(root.url)
                }
            }
        }
    }

    onClicked: {
        if (modelData?.page) {
            navigationView.safePush(modelData.page)
        }
    }
}
