import pygame
import random

# Define card values and image paths
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
card_images = {suit + card: f"cards/{suit}{card}.png" for suit in ["d", "c", "s", "h"] for card in card_values.keys()}

round_number = 1

# Function to load card image
def load_card_image(card, images):
  """Loads a card image from the provided dictionary of image paths.

  Args:
      card: A string representing the card (e.g., "d7" for the diamond 7).
      images: A dictionary mapping card names to image paths.

  Returns:
      The pygame Surface object representing the card image, 
      or None if the card image is not found.
  """
  image_path = images.get(card)
  if image_path:
    return pygame.image.load(image_path)
  else:
    return None


# Function to deal cards
def deal_cards(num_players, num_suits):
  player_cards = []
  for player in range(num_players):
    player_cards.append(random.sample(list(card_values.keys()), 13)[:13])
  return player_cards


# Function to draw a card on the screen
def draw_card(screen, card, x, y, images):
  """Draws a card image on the game screen.

  Args:
      screen: The pygame Surface object representing the game screen.
      card: A string representing the card (e.g., "d7" for the diamond 7).
      x: The x-coordinate of the top-left corner of the card image.
      y: The y-coordinate of the top-left corner of the card image.
      images: A dictionary mapping card names to image paths.
  """
  card_image = load_card_image(card, images)
  if card_image:
      # Resize the card image to a desired size
      new_width = 80  # Adjust width as needed
      new_height = 105  # Adjust height as needed
      card_image = pygame.transform.scale(card_image, (new_width, new_height))
      screen.blit(card_image, (x, y))


# Function for computer bidding logic (replace with your desired strategy)
def computer_bid(player_cards, diamond_value):
  """Simulates the computer's bidding logic.

  This function implements a simple bidding strategy where the computer 
  chooses the highest card it has that is at least half the value of the 
  auctioned diamond. If there are no such cards, it returns the lowest card 
  in its hand (or None if the hand is empty).

  Args:
      player_cards: A list of cards in the computer's hand.
      diamond_value: The value of the diamond being auctioned.

  Returns:
      The card chosen by the computer for its bid, or None if the computer 
      has no cards left.
  """
  eligible_cards = [card for card in player_cards if card_values[card] >= diamond_value // 2]
  if eligible_cards:
    return random.choice(eligible_cards)
  # Otherwise, check if the hand is empty before finding the minimum
  else:
    if player_cards:  # Check if there are any cards left
      return min(player_cards, key=card_values.get)
    else:
      return None  # Player has no cards left


# Function to handle bidding round
def bidding_round(screen, player_cards, diamond_card, font, player_points):
  """Conducts a bidding round for a single diamond.

  This function displays the auctioned diamond, prompts the human player for 
  a bid, simulates the computer's bid, and determines the winner(s) of the round.

  Args:
      screen: The pygame Surface object representing the game screen.
      player_cards: A list of cards in the human player's hand.
      diamond_card: A string representing the diamond being auctioned 
                     (e.g., "d7" for the diamond 7).
      font: A pygame Font object used for displaying text on the screen.
      player_points: A list containing the current point totals for each player.

  Returns:
      A tuple containing two elements:
          - A list of indices representing the winning players.
          - A list of cards representing the bids of each player.
  """
    
  # Display auctioned diamond
  diamond_value = card_values[diamond_card]
  print("card auctioned: ", diamond_value)
  draw_card(screen, f"d{diamond_card}", 100, 100, card_images)
  
  pygame.display.flip()
  text_surface = font.render(f"Player Points:", True, (255, 255, 255))
  screen.blit(text_surface, (100, 400))
  for i, points in enumerate(player_points):
    text_surface = font.render(f"  Player {i + 1}: {points} points", True, (255, 255, 255))
    screen.blit(text_surface, (100, 430 + 30 * i))

  # Display remaining cards
  text_surface = font.render(f"Cards Remaining: {len(player_cards[0])}", True, (255, 255, 255))
  screen.blit(text_surface, (100, 500))

  global round_number
  text_surface = font.render(f"Round : {round_number}", True, (255, 255, 255))
  screen.blit(text_surface, (100, 360))
  round_number += 1

  card_spacing = 82
  for i, card in enumerate(player_cards[0]):
    card_x, card_y = 110 + i * card_spacing, 600
    draw_card(screen, "c" + card, card_x, card_y, card_images)
  pygame.display.flip()

  # Get human player bid
  selected_card = None
  while not selected_card:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        # Check if clicked on a card in hand
        for i, card in enumerate(player_cards[0]):
          card_x, card_y = 200 + i * card_spacing, 600
          card_rect = pygame.Rect(card_x, card_y, 71, 96)
          if card_rect.collidepoint(pos):
            selected_card = card
            player_cards[0].remove(card)
            break

  # Display human player bid
  draw_card(screen, "c" + selected_card, 400, 100, card_images)
  text_surface = font.render(f"Your Bid: {selected_card}", True, (255, 255, 255))
  print("human: ", selected_card)
  screen.blit(text_surface, (400, 210))
  pygame.display.flip()

  # Simulate computer bid
  computer_card = computer_bid(player_cards[1], diamond_value)
  if computer_card:
    computer_x = 600
    draw_card(screen, "h" + computer_card, computer_x, 100, card_images)
    text_surface = font.render(f"Computer's Bid: {computer_card}", True, (255, 255, 255))
    print("comp: ", computer_card)
    screen.blit(text_surface, (computer_x, 210))
  else:
    text_surface = font.render(f"Computer has no cards left!", True, (255, 255, 255))
    screen.blit(text_surface, (600, 100))
  pygame.display.flip()

  bids = [selected_card, computer_card]
  highest_bid = max(card_values[card] for card in bids)
  winning_players = [i for i, card in enumerate(bids) if card_values[card] == highest_bid]

  return winning_players, bids


# Function to play the game
def play_game(num_players=2, num_suits=2):
  # Initialize Pygame
  pygame.init()
  screen = pygame.display.set_mode((1200, 1000))
  pygame.display.set_caption("Diamonds")
  font = pygame.font.Font(None, 32)

  # Deal cards
  player_cards = deal_cards(num_players, num_suits)

  # Track player points
  player_points = [0] * num_players

  # Diamond deck
  diamond_deck = list(card_values.keys())
  random.shuffle(diamond_deck)

  # Game loop
  game_over = False
  while not game_over:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      
    # Clear the screen before each round
    screen.fill((0, 80, 0))

    # Play a round
    if diamond_deck:
      diamond_card = diamond_deck.pop()
      diamond_value = card_values[diamond_card]
      winning_players, bids = bidding_round(screen, player_cards, diamond_card, font, player_points)
      print(bids)
      # Award points based on winner
      if winning_players:
      # Split the diamond value equally among winners
        points_per_player = diamond_value / len(winning_players)
        print("winning_players",winning_players)
        for winner in winning_players:
          player_points[winner] += points_per_player
        if card_values[bids[0]] > card_values[bids[1]]:
          text_surface = font.render(f"You won {diamond_value} points!", True, (255, 255, 255))
          screen.blit(text_surface, (100, 300))
        elif card_values[bids[0]] < card_values[bids[1]]: 
          text_surface = font.render(f"Computer won {diamond_value} points!", True, (255, 255, 255))
          screen.blit(text_surface, (100, 300))
        else:
          text_surface = font.render(f"Computer and You won {diamond_value/2} points each!", True, (255, 255, 255))
          screen.blit(text_surface, (100, 300))

    # Display player point totals after each round
      print("Bids",bids)
      print("Player 1 bid:",bids[0])
      print("Player 2 bid:", bids[1])
      print(f"\nPlayer Points:")
      for i, points in enumerate(player_points):
        print(f"  Player {i + 1}: {points} points")
    # Display remaining cards in the deck after each round
      print(f"\nCards Remaining in Deck: {len(diamond_deck)}")

      # Display results with a delay
      pygame.display.flip()
      pygame.time.wait(3000)  # Wait for 2 seconds (adjust as needed)

    else:
      # Game Over
      game_over = True
      winning_player = player_points.index(max(player_points))
      text_surface = font.render(f"You have {player_points[0]} points!", True, (255, 255, 255))
      screen.blit(text_surface, (480, 400))
      text_surface = font.render(f"Computer has {player_points[1]} points!", True, (255, 255, 255))
      screen.blit(text_surface, (480, 480))
      if(winning_player == 1):
        text_surface = font.render(f"COMPUTER WON", True, (255, 255, 255))
        screen.blit(text_surface, (480, 560))
      else:
        text_surface = font.render(f"YOU WON", True, (255, 255, 255))
        screen.blit(text_surface, (480, 560))
      pygame.display.flip()
      pygame.time.wait(5000)

  # Quit Pygame
  pygame.quit()

# Run the game
play_game()

