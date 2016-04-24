# -*- coding: utf-8 -*-

from .base import FSlider


class _BasicSlider(FSlider):
    '''slider with basic style'''
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app

        theme = app.theme_manager.current_theme
        self._style_str = '''
            QSlider::groove:horizontal {{
                background: {1};
                height: 4px;
                border-radius: 2px;
            }}
            QSlider::handle:horizontal {{
                background: {2};
                width: 16px;
                margin: -6px 0;
                border-radius: 8px;
            }}
            QSlider::sub-page:horizontal {{
                background: {3};
            }}
        '''.format(self.objectName(),
                   theme.foreground.name(),
                   theme.color4.name(),
                   theme.color0.name())
        self.set_theme_style()

    def set_theme_style(self):
        self.setStyleSheet(self._style_str)
