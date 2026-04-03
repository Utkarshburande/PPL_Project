import pygame
import random
import sys
import math

pygame.init()

# --- Config ---
WIDTH, HEIGHT = 1000, 600
FPS = 60

# Colors
BG_COLOR = (30, 30, 46)     # Dark Catppuccin-like BG
NODE_COLOR_1 = (137, 180, 250) # Blue
NODE_COLOR_2 = (243, 139, 168) # Red
NODE_COLOR_R = (166, 227, 161) # Green
TEXT_COLOR = (17, 17, 27)
HIGHLIGHT_COLOR = (249, 226, 175) # Yellow
LINE_COLOR = (180, 190, 254)

# Fonts
font_large = pygame.font.SysFont("segoeui", 28, bold=True)
font_small = pygame.font.SysFont("segoeui", 20, bold=True)
font_ui = pygame.font.SysFont("segoeui", 22)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.clicked = False

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, width=2, border_radius=10)
        
        text_surf = font_ui.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

class VisualNode:
    def __init__(self, coeff, power, start_x, start_y, color):
        self.coeff = coeff
        self.power = power
        
        self.x = start_x
        self.y = start_y
        self.target_x = start_x
        self.target_y = start_y
        
        self.color = color
        self.next = None
        
        self.width = 90
        self.height = 50
        self.highlighted = False

    def update(self):
        # Lerp towards target position for smooth animation
        speed = 0.15
        self.x += (self.target_x - self.x) * speed
        self.y += (self.target_y - self.y) * speed

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Draw Glow/Highlight
        if self.highlighted:
            glow_rect = rect.inflate(8, 8)
            pygame.draw.rect(surface, HIGHLIGHT_COLOR, glow_rect, border_radius=12)

        # Draw main node
        pygame.draw.rect(surface, self.color, rect, border_radius=10)
        
        # Format text, e.g., "5x^2" or "-3x" or "4"
        term_text = ""
        c = self.coeff
        p = self.power
        
        if c == -1 and p != 0: term_text += "-"
        elif c != 1 or p == 0: term_text += str(c)
        
        if p > 0: term_text += "x"
        
        # Render text
        parts = []
        parts.append((term_text, font_large))
        
        # Calculate total width for centering
        text_w = sum(font.size(t)[0] for t, font in parts)
        if p > 1:
            text_w += font_small.size(f"^{p}")[0]
            
        start_x = self.x + (self.width - text_w) // 2
        
        # Render main term
        main_surf = font_large.render(term_text, True, TEXT_COLOR)
        surface.blit(main_surf, (start_x, self.y + 8))
        
        # Render power superscript
        if p > 1:
            power_surf = font_small.render(f"{p}", True, TEXT_COLOR)
            surface.blit(power_surf, (start_x + main_surf.get_width(), self.y + 4))

        # Draw Next Pointer Line
        if self.next:
            start_pos = (self.x + self.width, self.y + self.height // 2)
            end_pos = (self.next.x, self.next.y + self.height // 2)
            pygame.draw.line(surface, LINE_COLOR, start_pos, end_pos, 3)
            
            # Simple Arrowhead
            angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
            pygame.draw.polygon(surface, LINE_COLOR, [
                end_pos,
                (end_pos[0] - 10 * math.cos(angle - math.pi/6), end_pos[1] - 10 * math.sin(angle - math.pi/6)),
                (end_pos[0] - 10 * math.cos(angle + math.pi/6), end_pos[1] - 10 * math.sin(angle + math.pi/6))
            ])


class VisualPolynomial:
    def __init__(self, y_pos, color):
        self.head = None
        self.y_pos = y_pos
        self.start_x = 50
        self.spacing = 130
        self.color = color
        
    def add_node(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.update_targets()
            
    def update_targets(self):
        current = self.head
        idx = 0
        while current:
            current.target_x = self.start_x + idx * self.spacing
            current.target_y = self.y_pos
            current = current.next
            idx += 1
            
    def update(self):
        current = self.head
        while current:
            current.update()
            current = current.next
            
    def draw(self, surface):
        current = self.head
        while current:
            current.draw(surface)
            current = current.next
            
    def clear(self):
        self.head = None


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Linked List Polynomial Addition")
        self.clock = pygame.time.Clock()
        
        self.poly1 = VisualPolynomial(150, NODE_COLOR_1)
        self.poly2 = VisualPolynomial(300, NODE_COLOR_2)
        self.poly_res = VisualPolynomial(450, NODE_COLOR_R)
        
        # Algorithm State
        self.p1_curr = None
        self.p2_curr = None
        self.state = "IDLE" # IDLE, ADDING, DONE
        
        self.buttons = [
            Button(20, 20, 180, 45, "Generate Random", (137, 180, 250), (180, 190, 254)),
            Button(220, 20, 150, 45, "Step (+)", (166, 227, 161), (148, 226, 213)),
            Button(390, 20, 150, 45, "Add All", (249, 226, 175), (250, 179, 135)),
            Button(560, 20, 150, 45, "Reset", (243, 139, 168), (235, 160, 172))
        ]
        
        self.generate_random()

    def generate_random(self):
        self.poly1.clear()
        self.poly2.clear()
        self.poly_res.clear()
        
        # Generate Poly 1
        num_terms1 = random.randint(3, 5)
        powers1 = sorted(random.sample(range(0, 7), num_terms1), reverse=True)
        for p in powers1:
            coeff = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            self.poly1.add_node(VisualNode(coeff, p, -100, 150, NODE_COLOR_1))
            
        # Generate Poly 2
        num_terms2 = random.randint(3, 5)
        powers2 = sorted(random.sample(range(0, 7), num_terms2), reverse=True)
        for p in powers2:
            coeff = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            self.poly2.add_node(VisualNode(coeff, p, -100, 300, NODE_COLOR_2))
            
        self.p1_curr = self.poly1.head
        self.p2_curr = self.poly2.head
        self.state = "ADDING"

    def clear_highlights(self):
        curr = self.poly1.head
        while curr: curr.highlighted = False; curr = curr.next
        curr = self.poly2.head
        while curr: curr.highlighted = False; curr = curr.next

    def perform_step(self):
        if self.state != "ADDING":
            return
            
        self.clear_highlights()
            
        if self.p1_curr is None and self.p2_curr is None:
            self.state = "DONE"
            return
            
        if self.p1_curr: self.p1_curr.highlighted = True
        if self.p2_curr: self.p2_curr.highlighted = True

        new_node = None

        if self.p1_curr and self.p2_curr:
            if self.p1_curr.power > self.p2_curr.power:
                new_node = VisualNode(self.p1_curr.coeff, self.p1_curr.power, self.p1_curr.x, self.p1_curr.y, NODE_COLOR_R)
                self.p1_curr = self.p1_curr.next
            elif self.p2_curr.power > self.p1_curr.power:
                new_node = VisualNode(self.p2_curr.coeff, self.p2_curr.power, self.p2_curr.x, self.p2_curr.y, NODE_COLOR_R)
                self.p2_curr = self.p2_curr.next
            else:
                sum_coeff = self.p1_curr.coeff + self.p2_curr.coeff
                if sum_coeff != 0:
                    mid_x = (self.p1_curr.x + self.p2_curr.x) / 2
                    mid_y = (self.p1_curr.y + self.p2_curr.y) / 2
                    new_node = VisualNode(sum_coeff, self.p1_curr.power, mid_x, mid_y, NODE_COLOR_R)
                self.p1_curr = self.p1_curr.next
                self.p2_curr = self.p2_curr.next
        elif self.p1_curr:
            new_node = VisualNode(self.p1_curr.coeff, self.p1_curr.power, self.p1_curr.x, self.p1_curr.y, NODE_COLOR_R)
            self.p1_curr = self.p1_curr.next
        elif self.p2_curr:
            new_node = VisualNode(self.p2_curr.coeff, self.p2_curr.power, self.p2_curr.x, self.p2_curr.y, NODE_COLOR_R)
            self.p2_curr = self.p2_curr.next

        if new_node:
            self.poly_res.add_node(new_node)
            
        if self.p1_curr is None and self.p2_curr is None:
            self.state = "DONE"
            self.clear_highlights()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                for btn in self.buttons:
                    btn.handle_event(event)
                    if btn.clicked:
                        if btn.text == "Generate Random":
                            self.generate_random()
                        elif btn.text == "Step (+)":
                            self.perform_step()
                        elif btn.text == "Add All":
                            while self.state == "ADDING":
                                self.perform_step()
                        elif btn.text == "Reset":
                            self.poly_res.clear()
                            self.p1_curr = self.poly1.head
                            self.p2_curr = self.poly2.head
                            self.state = "ADDING"
                            self.clear_highlights()
                        btn.clicked = False # Reset click flag
            
            # Updates
            self.poly1.update()
            self.poly2.update()
            self.poly_res.update()

            # Draw
            self.screen.fill(BG_COLOR)
            
            # Titles
            title_p1 = font_ui.render("Polynomial 1", True, NODE_COLOR_1)
            title_p2 = font_ui.render("Polynomial 2", True, NODE_COLOR_2)
            title_res = font_ui.render("Result Polynomial", True, NODE_COLOR_R)
            
            self.screen.blit(title_p1, (50, 110))
            self.screen.blit(title_p2, (50, 260))
            self.screen.blit(title_res, (50, 410))

            # Draw polynomials
            self.poly1.draw(self.screen)
            self.poly2.draw(self.screen)
            self.poly_res.draw(self.screen)
            
            # Status text
            if self.state == "DONE":
                status = font_large.render("Addition Complete!", True, HIGHLIGHT_COLOR)
                self.screen.blit(status, (WIDTH - 250, 30))

            for btn in self.buttons:
                btn.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.run()
