from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase

class TitoloViewlet(ViewletBase):
        index = ViewPageTemplateFile('templates/titolo.pt')

        def update(self):
                super(TitoloViewlet, self).update()

                portal = self.portal_state.portal()
                self.titolo = self.portal_state.portal_title()

