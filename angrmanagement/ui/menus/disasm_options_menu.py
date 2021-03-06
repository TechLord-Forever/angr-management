
from .menu import Menu, MenuEntry, MenuSeparator


class DisasmOptionsMenu(Menu):
    def __init__(self, disasm_view):
        super(DisasmOptionsMenu, self).__init__("", parent=disasm_view)

        self._show_address_action = MenuEntry('Show &address', self._show_address, checkable=True,
                                              checked=self.parent.show_address
                                              )
        self._show_variable_action = MenuEntry('Show &variable', self._show_variable, checkable=True,
                                               checked=self.parent.show_variable)
        self._show_variable_ident_action = MenuEntry('Show variable &identifiers', self._show_variable_identifier,
                                                     checkable=True,
                                                     checked=self.parent.show_variable_identifier
                                                     )

        self.entries.extend([
            self._show_address_action,
            self._show_variable_action,
            self._show_variable_ident_action,
        ])

    def _show_address(self):
        checked = self._show_address_action.checked
        self.parent.toggle_show_address(checked)

    def _show_variable(self):
        checked = self._show_variable_action.checked
        self.parent.toggle_show_variable(checked)

    def _show_variable_identifier(self):
        checked = self._show_variable_ident_action.checked
        self.parent.toggle_show_variable_identifier(checked)
