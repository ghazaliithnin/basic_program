# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:42:29 2020

@author: user
"""
# colors for the bboxes
COLORS = ['red', 'blue', 'yellow', 'pink', 'cyan', 'green', 'black']

def mouseClick(self, event):
    if self.STATE['click'] == 0:
        self.STATE['x'], self.STATE['y'] = event.x, event.y
    else:
        x1, x2 = min(self.STATE['x'], event.x), max(self.STATE['x'], event.x)
        y1, y2 = min(self.STATE['y'], event.y), max(self.STATE['y'], event.y)
        self.bboxList.append((x1, y1, x2, y2))
        self.bboxIdList.append(self.bboxId)
        self.bboxId = None
        self.listbox.insert(END, '(%d, %d) -> (%d, %d)' %(x1, y1, x2, y2))
        self.listbox.itemconfig(len(self.bboxIdList) - 1, fg = COLORS[(len(self.bboxIdList) - 1) % len(COLORS)])
    self.STATE['click'] = 1 - self.STATE['click']
