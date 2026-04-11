import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml
import RinUI

FluentWindow {
    id: window
    width: 900
    height: 600
    minimumWidth: 600
    minimumHeight: 400
    maximumWidth: 16777215
    maximumHeight: 16777215
    visible: true
    title: "AppStore"
    defaultPage: Qt.resolvedUrl("pages/Home.qml")

    navigationItems: [
        {
            title: qsTr("Home"),
            page: Qt.resolvedUrl("pages/Home.qml"),
            icon: "ic_fluent_home_20_filled",
        },
        {
            title: qsTr("Settings"),
            page: Qt.resolvedUrl("pages/Settings.qml"), 
            icon: "ic_fluent_settings_20_regular"
        }
    ]
}
